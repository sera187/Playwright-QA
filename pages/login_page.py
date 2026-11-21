from playwright.sync_api import Page


class LoginPage:
    URL = "https://practicesoftwaretesting.com/auth/login"

    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("[data-test=\"email\"]")
        self.password_input = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-submit\"]")
        self.login_error = page.locator("[data-test=\"login-error\"]")
        self.email_error = page.locator("[data-test=\"email-error\"]")

    def open(self):
        self.page.goto(self.URL)

    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()