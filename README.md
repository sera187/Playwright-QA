# Playwright QA Automation

End-to-end UI tests for the [Practice Software Testing](https://practicesoftwaretesting.com) demo web shop, written in Python with Playwright and pytest.

## What it tests

- **Login flows** (`test_login.py`): valid login, invalid email format, unregistered email, and wrong password, checking the right validation and error messages.
- **Cart flow** (`test_cart.py`): opening a product and adding it to the cart, verifying the cart updates correctly.

## Tech stack

- Python
- Playwright
- pytest

## How to run

```bash
# install dependencies
pip install pytest-playwright
playwright install

# run all tests
pytest

# run with a visible browser
pytest --headed
```

## About

Built as part of my hands-on learning in test automation, focusing on reliable locators, assertions, and clean, readable tests.
