from playwright.sync_api import Page


class ProductPage:
    URL = "https://practicesoftwaretesting.com"

    def __init__(self, page: Page):
        self.page = page
        self.product_name = page.locator("[data-test=\"product-name\"]")
        self.add_to_cart_button = page.locator("[data-test=\"add-to-cart\"]")
        self.cart_quantity = page.locator("[data-test=\"cart-quantity\"]")

    def open(self):
        self.page.goto(self.URL)

    def open_product(self, name):
        self.page.get_by_role("link", name=name).click()

    def add_to_cart(self):
        self.add_to_cart_button.click()