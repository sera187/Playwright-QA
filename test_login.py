from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_invalid_email(page: Page):
    """Login with an invalid email format should show a validation error."""
    login = LoginPage(page)
    login.open()
    login.login("sera123", "1234567890")
    expect(login.email_error).to_contain_text("Email format is invalid")


def test_not_in_DB_email(page: Page):
    """Login with a valid but unregistered email should be rejected."""
    login = LoginPage(page)
    login.open()
    login.login("sera18@hotmail.gr", "1234567890")
    expect(login.login_error).to_contain_text("Invalid email or password")


def test_invalid_pass(page: Page):
    """Login with a registered email but wrong password should be rejected."""
    login = LoginPage(page)
    login.open()
    login.login("admin@practicesoftwaretesting.com", "123")
    expect(login.login_error).to_contain_text("Invalid email or password")


def test_successful_login(page: Page):
    """Login with valid credentials should redirect to the account page."""
    login = LoginPage(page)
    login.open()
    login.login("customer@practicesoftwaretesting.com", "welcome01")
    expect(page).to_have_url("https://practicesoftwaretesting.com/account")