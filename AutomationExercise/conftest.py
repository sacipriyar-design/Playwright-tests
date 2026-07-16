from playwright.sync_api import sync_playwright
import pytest
from pages.contact_page import ContactPage
from pages.login_page import LoginPage
from pages.cart_page import cartpage
EMAIL="Test1@email.com"
PASSWORD="password123"
@pytest.fixture
def test_goto_page():
    with sync_playwright() as p:
        Browser = p.chromium.launch(headless=True)
        page=Browser.new_page()
        #page.goto("https://automationexercise.com/")
        yield page
        Browser.close()
@pytest.fixture
def contact_page(test_goto_page):
    page=test_goto_page
    page.goto("https://automationexercise.com/contact_us")
    return ContactPage(page)

@pytest.fixture
def cart_page_login(test_goto_page):
    page = test_goto_page
    login_page = LoginPage(page)
    login_page.goto_page()
    login_page.login(EMAIL,PASSWORD)
    
    cart = cartpage(page)
    cart.navigate_to_products()
    return cart