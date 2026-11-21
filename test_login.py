from playwright.sync_api import Page, expect

#Negative Cases
def test_invalid_email(page: Page):
    page.goto("https://practicesoftwaretesting.com/auth/login")
    page.locator("[data-test=\"email\"]").fill("sera123")
    page.locator("[data-test=\"password\"]").fill("1234567890")
    page.locator("[data-test=\"login-submit\"]").click()
    expect(page.locator("[data-test=\"email-error\"]")).to_contain_text("Email format is invalid")
 

def test_email_notInDB(page: Page):
    page.goto("https://practicesoftwaretesting.com/auth/login")
    page.locator("[data-test=\"email\"]").fill("sera18@hotmail.gr")
    page.locator("[data-test=\"password\"]").fill("1234567890")
    page.locator("[data-test=\"login-submit\"]").click()
    expect(page.locator("[data-test=\"login-error\"]")).to_contain_text("Invalid email or password")
    
   
def test_invalid_pass(page: Page):
    page.goto("https://practicesoftwaretesting.com/auth/login")
    page.locator("[data-test=\"email\"]").fill("admin@practicesoftwaretesting.com")
    page.locator("[data-test=\"password\"]").fill("123")
    page.locator("[data-test=\"login-submit\"]").click()
    expect(page.locator("[data-test=\"login-error\"]")).to_contain_text("Invalid email or password")


def test_fill_onlypass(page: Page):
    page.goto("https://practicesoftwaretesting.com/auth/login")
    page.locator("[data-test=\"password\"]").fill("welcome01")
    page.locator("[data-test=\"login-submit\"]").click()
    expect(page.locator("[data-test=\"email-error\"]")).to_contain_text("Email is required")
 

def test_fill_onlymail(page: Page):
    page.goto("https://practicesoftwaretesting.com/auth/login")
    page.locator("[data-test=\"email\"]").fill("admin@practicesoftwaretesting.com")
    page.locator("[data-test=\"login-submit\"]").click()
    expect(page.locator("[data-test=\"password-error\"]")).to_contain_text("Password is required")


#Positive Case
def test_success_logIn(page: Page):
    page.goto("https://practicesoftwaretesting.com/auth/login")
    page.locator("[data-test=\"email\"]").fill("admin@practicesoftwaretesting.com")
    page.locator("[data-test=\"password\"]").fill("welcome01")
    page.locator("[data-test=\"login-submit\"]").click()
  