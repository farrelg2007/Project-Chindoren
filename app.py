# -*- coding: utf-8 -*-
import uuid
from flask import Flask, render_template, request, redirect, url_for, session, flash

from products import PRODUCTS, get_product, get_related, categories, format_price

app = Flask(__name__)
app.secret_key = "chindoren-dev-secret-change-me"

FREE_SHIPPING_THRESHOLD = 500000
SHIPPING_FLAT = 25000


@app.context_processor
def inject_globals():
    cart = session.get("cart", {})
    count = sum(item["qty"] for item in cart.values())
    return {"cart_count": count, "format_price": format_price, "all_categories": categories()}


def _cart_lines():
    cart = session.get("cart", {})
    lines = []
    subtotal = 0
    for key, item in cart.items():
        product = get_product(item["product_id"])
        if not product:
            continue
        line_total = product["price"] * item["qty"]
        subtotal += line_total
        lines.append({
            "key": key, "product": product, "qty": item["qty"],
            "size": item["size"], "color": item["color"], "line_total": line_total,
        })
    return lines, subtotal


@app.route("/")
def home():
    featured = [p for p in PRODUCTS if "bestseller" in p["tags"]][:4]
    newest = sorted(PRODUCTS, key=lambda p: (-p["drop"], p["id"]))[:4]
    current_drop = max(p["drop"] for p in PRODUCTS)
    return render_template("index.html", featured=featured, newest=newest,
                            current_drop=current_drop, cats=categories())


@app.route("/products")
def products_page():
    q = request.args.get("q", "").strip().lower()
    cat = request.args.get("cat", "All")
    sort = request.args.get("sort", "featured")

    items = list(PRODUCTS)
    if cat and cat != "All":
        items = [p for p in items if p["category"] == cat]
    if q:
        items = [p for p in items if q in p["name"].lower() or q in p["category"].lower()]

    if sort == "newest":
        items.sort(key=lambda p: (-p["drop"], p["id"]))
    elif sort == "price_asc":
        items.sort(key=lambda p: p["price"])
    elif sort == "price_desc":
        items.sort(key=lambda p: -p["price"])

    return render_template("shop.html", products=items, cat=cat, q=request.args.get("q", ""),
                            sort=sort, total=len(items))


@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = get_product(product_id)
    if not product:
        return render_template("404.html"), 404
    related = get_related(product)
    return render_template("product.html", product=product, related=related)


@app.route("/cart/add/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    product = get_product(product_id)
    if not product:
        return redirect(url_for("products_page"))

    size = request.form.get("size", product["sizes"][0])
    color = request.form.get("color", product["colors"][0])
    qty = max(1, min(int(request.form.get("qty", 1) or 1), product["stock"]))

    key = f"{product_id}|{size}|{color}"
    cart = session.get("cart", {})
    if key in cart:
        cart[key]["qty"] = min(cart[key]["qty"] + qty, product["stock"])
    else:
        cart[key] = {"product_id": product_id, "size": size, "color": color, "qty": qty}
    session["cart"] = cart
    flash(f"{product['name']} added to your bag.", "success")
    return redirect(url_for("product_detail", product_id=product_id))


@app.route("/cart/update", methods=["POST"])
def update_cart():
    cart = session.get("cart", {})
    for key in list(cart.keys()):
        qty_raw = request.form.get(f"qty_{key}")
        if qty_raw is None:
            continue
        qty = int(qty_raw)
        if qty <= 0:
            cart.pop(key, None)
        else:
            product = get_product(cart[key]["product_id"])
            cap = product["stock"] if product else qty
            cart[key]["qty"] = min(qty, cap)
    session["cart"] = cart
    flash("Bag updated.", "success")
    return redirect(url_for("cart_page"))


@app.route("/cart/remove/<path:key>", methods=["POST"])
def remove_from_cart(key):
    cart = session.get("cart", {})
    cart.pop(key, None)
    session["cart"] = cart
    flash("Item removed.", "success")
    return redirect(url_for("cart_page"))


@app.route("/cart")
def cart_page():
    lines, subtotal = _cart_lines()
    shipping = 0 if subtotal >= FREE_SHIPPING_THRESHOLD or subtotal == 0 else SHIPPING_FLAT
    total = subtotal + shipping
    return render_template("cart.html", lines=lines, subtotal=subtotal, shipping=shipping,
                            total=total, threshold=FREE_SHIPPING_THRESHOLD)


@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    lines, subtotal = _cart_lines()
    if not lines and request.method == "GET":
        return redirect(url_for("cart_page"))

    shipping = 0 if subtotal >= FREE_SHIPPING_THRESHOLD else SHIPPING_FLAT
    total = subtotal + shipping

    if request.method == "POST":
        order = {
            "id": "CHD-" + uuid.uuid4().hex[:8].upper(),
            "name": request.form.get("name", "").strip(),
            "email": request.form.get("email", "").strip(),
            "address": request.form.get("address", "").strip(),
            "city": request.form.get("city", "").strip(),
            "postcode": request.form.get("postcode", "").strip(),
            "phone": request.form.get("phone", "").strip(),
            "payment": request.form.get("payment", "Bank Transfer"),
            "lines": [{"name": l["product"]["name"], "size": l["size"], "color": l["color"],
                       "qty": l["qty"], "line_total": l["line_total"]} for l in lines],
            "subtotal": subtotal, "shipping": shipping, "total": total,
        }
        session["last_order"] = order
        session["cart"] = {}
        return redirect(url_for("order_success"))

    return render_template("checkout.html", lines=lines, subtotal=subtotal,
                            shipping=shipping, total=total)


@app.route("/order/success")
def order_success():
    order = session.get("last_order")
    if not order:
        return redirect(url_for("home"))
    return render_template("success.html", order=order)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
