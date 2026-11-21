from playwright.sync_api import Page, expect

BASE_URL = "https://practicesoftwaretesting.com"

def test_add_product_to_cart(page: Page):
    page.goto(BASE_URL)
    page.get_by_role("link",name="Bolt Cutters").click()
    expect(page.locator("[data-test=\"product-name\"]")).to_contain_text("Bolt Cutters")
    page.locator("[data-test=\"add-to-cart\"]").click()
    page.locator("[data-test=\"increase-quantity\"]").click()
    page.locator("[data-test=\"add-to-cart\"]").click()
    page.pause()
    expect(page.locator("[data-test=\"cart-quantity\"]")).to_have_text("1")
   

