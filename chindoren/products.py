# -*- coding: utf-8 -*-
"""Static product catalog for Chindoren."""

PRODUCTS = [
    {
        "id": 1, "sku": "CHD-HD-01", "name": "Ink Static Hoodie", "category": "Apparel",
        "price": 549000, "compare_at": 649000, "drop": 3, "icon": "hoodie",
        "colors": ["Ink Black", "Bone"], "sizes": ["S", "M", "L", "XL"],
        "description": "Heavyweight 400gsm fleece with a garment-dyed finish and a dropped shoulder cut. "
                        "The static-line graphic across the back channels the brand's broadcast motif.",
        "tags": ["new", "bestseller"], "stock": 18,
    },
    {
        "id": 2, "sku": "CHD-TS-02", "name": "Frequency Tee", "category": "Apparel",
        "price": 219000, "compare_at": None, "drop": 3, "icon": "tee",
        "colors": ["Bone", "Ink Black", "Cobalt"], "sizes": ["S", "M", "L", "XL"],
        "description": "Mid-weight 220gsm combed cotton, boxy fit, with a screen-printed frequency chart on the chest.",
        "tags": ["new"], "stock": 32,
    },
    {
        "id": 3, "sku": "CHD-TS-03", "name": "Static Logo Tee", "category": "Apparel",
        "price": 199000, "compare_at": None, "drop": 2, "icon": "tee",
        "colors": ["Ink Black", "Bone"], "sizes": ["S", "M", "L", "XL"],
        "description": "Our everyday tee. Clean logo hit at the chest, relaxed fit, built to be lived in.",
        "tags": [], "stock": 40,
    },
    {
        "id": 4, "sku": "CHD-JK-04", "name": "Signal Jacket", "category": "Apparel",
        "price": 899000, "compare_at": None, "drop": 3, "icon": "jacket",
        "colors": ["Ink Black"], "sizes": ["S", "M", "L", "XL"],
        "description": "A coach jacket cut from a matte nylon shell, taped seams, and a broadcast-yellow interior lining.",
        "tags": ["new", "limited"], "stock": 9,
    },
    {
        "id": 5, "sku": "CHD-CP-05", "name": "Low-Freq Cap", "category": "Headwear",
        "price": 189000, "compare_at": None, "drop": 2, "icon": "cap",
        "colors": ["Ink Black", "Cobalt"], "sizes": ["One Size"],
        "description": "A low-profile six-panel cap with a curved brim and an embroidered dial mark.",
        "tags": ["bestseller"], "stock": 26,
    },
    {
        "id": 6, "sku": "CHD-BN-06", "name": "Static Beanie", "category": "Headwear",
        "price": 149000, "compare_at": None, "drop": 1, "icon": "beanie",
        "colors": ["Ink Black", "Bone"], "sizes": ["One Size"],
        "description": "Ribbed knit beanie in a heavyweight cotton blend, finished with a woven tab.",
        "tags": [], "stock": 21,
    },
    {
        "id": 7, "sku": "CHD-TB-07", "name": "Carrier Tote", "category": "Accessories",
        "price": 159000, "compare_at": None, "drop": 2, "icon": "tote",
        "colors": ["Bone", "Ink Black"], "sizes": ["One Size"],
        "description": "Heavy canvas tote with reinforced handles, sized for a day's carry.",
        "tags": [], "stock": 30,
    },
    {
        "id": 8, "sku": "CHD-SK-08", "name": "Dial Socks (2-Pack)", "category": "Accessories",
        "price": 89000, "compare_at": None, "drop": 1, "icon": "socks",
        "colors": ["Mixed"], "sizes": ["One Size"],
        "description": "Two pairs of crew socks knit with a dial-mark jacquard at the ankle.",
        "tags": [], "stock": 50,
    },
    {
        "id": 9, "sku": "CHD-PN-09", "name": "Signal Pin Set", "category": "Accessories",
        "price": 69000, "compare_at": None, "drop": 1, "icon": "pin",
        "colors": ["Silver", "Gold"], "sizes": ["One Size"],
        "description": "A set of three hard-enamel pins pulled from the brand's dial and static iconography.",
        "tags": ["new"], "stock": 45,
    },
    {
        "id": 10, "sku": "CHD-PR-10", "name": "Transmission Print", "category": "Prints",
        "price": 249000, "compare_at": None, "drop": 2, "icon": "print",
        "colors": ["Ink Black"], "sizes": ["A2"],
        "description": "A giclee print of the season's transmission chart artwork, on 250gsm archival stock.",
        "tags": ["limited"], "stock": 12,
    },
    {
        "id": 11, "sku": "CHD-PR-11", "name": "Dial Chart Print", "category": "Prints",
        "price": 249000, "compare_at": None, "drop": 1, "icon": "print",
        "colors": ["Ink Black"], "sizes": ["A2"],
        "description": "A giclee print mapping the brand's dial marks across a gridded chart, archival stock.",
        "tags": [], "stock": 14,
    },
    {
        "id": 12, "sku": "CHD-MG-12", "name": "Static Mug", "category": "Accessories",
        "price": 119000, "compare_at": None, "drop": 1, "icon": "mug",
        "colors": ["Bone"], "sizes": ["One Size"],
        "description": "A 350ml stoneware mug with an in-glaze static ring, dishwasher and microwave safe.",
        "tags": [], "stock": 28,
    },
]


def get_product(product_id):
    for p in PRODUCTS:
        if p["id"] == int(product_id):
            return p
    return None


def get_related(product, limit=4):
    return [p for p in PRODUCTS if p["category"] == product["category"] and p["id"] != product["id"]][:limit]


def categories():
    seen = []
    for p in PRODUCTS:
        if p["category"] not in seen:
            seen.append(p["category"])
    return seen


def format_price(amount):
    return "Rp" + "{:,.0f}".format(amount).replace(",", ".")
