import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app


def test_success_page_shows_qris_when_payment_is_qris():
    client = app.test_client()
    with client.session_transaction() as sess:
        sess['last_order'] = {
            'id': 'CHD-TEST',
            'name': 'Test User',
            'email': 'test@example.com',
            'address': '123 Street',
            'city': 'Bandung',
            'postcode': '40123',
            'phone': '0812',
            'payment': 'QRIS',
            'lines': [],
            'subtotal': 100000,
            'shipping': 0,
            'total': 100000,
        }

    response = client.get('/order/success')
    assert response.status_code == 200
    assert 'qr.png' in response.get_data(as_text=True)
    assert 'Scan QRIS' in response.get_data(as_text=True)


def test_homepage_newest_section_uses_product_image():
    client = app.test_client()

    response = client.get('/')
    html = response.get_data(as_text=True)

    assert response.status_code == 200
    assert 'img/signal_jacket.jpeg' in html
    assert 'Signal Jacket' in html
