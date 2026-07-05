# Chindoren — v2

A redesigned version of the Chindoren storefront. Same Flask/session-cart architecture as
before (no database, no real payment gateway — still a prototype), rebuilt with a new visual
identity and a cleaned-up, non-duplicated layout.

## What changed from the previous version

- **New look**: moved from the light cream template look to a dark, "broadcast signal" identity
  built around the actual logo and banner photo you sent — cobalt blue accent, warm terracotta
  for bestseller badges, Space Grotesk + Inter + JetBrains Mono type system.
- **Real hero**: the homepage hero now uses your banner photo directly, with a gradient overlay
  so the headline stays readable.
- **De-duplicated UI**: one filter bar (was scattered across pills + a separate dropdown block),
  one card component reused everywhere (home, shop, related products), one badge system, one
  footer link structure — no repeated or conflicting sections.
- Simplified the per-product SVG icons down to one clean line-art icon per category (hoodie,
  tee, jacket, cap, beanie, tote, socks, pin, print, mug) instead of one bespoke icon per SKU,
  so the visual language is more consistent.
- Kept every route, cart/session behavior, shipping rule, and checkout flow from the original
  app — this is a visual and structural rebuild, not a feature rewrite.

## Run it locally

```bash
pip install flask
python3 app.py
```

Then open `http://127.0.0.1:5000`.

## Structure

```
app.py                  Flask routes (same 8 routes + 404 handler as before)
products.py             Product catalog (12 products, 4 categories)
templates/
  base.html              Header, nav, footer, flash messages
  index.html             Homepage (hero, categories, drop banner, bestsellers, newest)
  shop.html              Product listing with filters/search/sort
  product.html           Product detail + related products
  cart.html              Bag with qty update / remove
  checkout.html          Shipping + payment form
  success.html           Order confirmation
  404.html               Custom not-found page
  _icons.html            Shared line-art icon set (Jinja macro)
static/
  css/style.css          Full design system (tokens, components, responsive rules)
  img/                   Logo (light/dark transparent versions) + hero banner
```

## Before deploying

- Replace `app.secret_key` in `app.py` with a real secret.
- Swap the in-memory `products.py` list for a real database if you need persistence.
- Wire up a real payment gateway (Midtrans/Xendit) — checkout currently just simulates an order.
