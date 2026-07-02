from pages.cart_page import cartpage
from pages.Chekout_page import paymentpage
import csv
import pytest

def test_checkout(test_goto_page):
    
    cart=cartpage(test_goto_page)
   
    test_goto_page.goto("https://automationexercise.com/login")
    test_goto_page.get_by_text("Signup / Login").click()
    test_goto_page.fill("[data-qa='login-email']","Test1@email.com")
    test_goto_page.fill("[data-qa='login-password']","password123")
    test_goto_page.locator("button",has_text="Login").click()
    test_goto_page.wait_for_timeout(3000)

    cart.navigate_to_products()
    cart.search_product("Men Tshirt")
    test_goto_page.wait_for_timeout(3000)
    cart.add_to_cart()
    cart.view_cart()
    assert "view_cart" in test_goto_page.url

    checkout=paymentpage(test_goto_page)
    checkout.proceed_checkout()
    checkout.payment_page("abc","123456789015","878","09","2026")
    



def test_checkout_without_Login(test_goto_page):
    test_goto_page.goto("https://automationexercise.com/products")
    cart=cartpage(test_goto_page)
    cart.page.wait_for_timeout(3000)

    cart.navigate_to_products()
    cart.search_product("Men Tshirt")
    cart.add_to_cart()
    cart.view_cart()
    assert "view_cart" in test_goto_page.url
    
    cart.page.get_by_text("Proceed To Checkout").click()
    modal_text = test_goto_page.locator("#checkoutModal")
    assert modal_text.is_visible()
    assert "Register / Login account to proceed on checkout" in modal_text.inner_text()