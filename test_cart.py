from playwright.sync_api import Page, expect
from pages.product_page import ProductPage


def test_add_product_to_cart(page: Page):
    """Adding a product to the cart should update the cart quantity."""
    product = ProductPage(page)
    product.open()
    product.open_product("Bolt Cutters")
    expect(product.product_name).to_contain_text("Bolt Cutters")
    product.add_to_cart()
    expect(product.cart_quantity).to_have_text("1")