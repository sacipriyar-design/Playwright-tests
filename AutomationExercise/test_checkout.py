from pages.cart_page import cartpage
from pages.Chekout_page import paymentpage
import csv
import pytest
import re
from playwright.sync_api import expect

def test_checkout(cart_page_login):
    cart=cart_page_login
    cart.search_product("Men Tshirt")
    expect(cart.page.locator(".product-image-wrapper").first).to_be_visible()
    results = cart.get_all_search_results()
    assert "Men Tshirt" in results
    cart.add_to_cart()
    cart.view_cart()
    assert "view_cart" in cart.page.url

    checkout=paymentpage(cart.page)
    checkout.proceed_checkout()
    checkout.payment_page("abc","123456789015","878","09","2026")
    expect(cart.page).to_have_url(re.compile("payment_done"))





def test_checkout_without_Login(test_goto_page):
    test_goto_page.goto("https://automationexercise.com/products")
    cart=cartpage(test_goto_page)
   

    cart.navigate_to_products()

    cart.search_product("")
    expect(test_goto_page.locator(".product-image-wrapper").first).to_be_visible()
    results = cart.get_all_search_results()
    print(results)
    product_name = cart.get_product_name()
    assert product_name == "Blue Top"
    cart.add_to_cart()
    cart.view_cart()
    expect(test_goto_page).to_have_url(re.compile("view_cart"))
   
    cart.page.get_by_text("Proceed To Checkout").click()
    modal_text = test_goto_page.locator("#checkoutModal")
    expect(modal_text).to_be_visible()
    assert "Register / Login account to proceed on checkout" in modal_text.inner_text()
    expect(modal_text).to_contain_text("Register / Login account to proceed on checkout")
def test_search_product(test_goto_page):
    test_goto_page.goto("https://automationexercise.com/products")
    cart=cartpage(test_goto_page)
    cart.navigate_to_products()
    cart.search_product("Women")
    expect(test_goto_page.locator(".product-image-wrapper").first).to_be_visible()
    result = cart.get_all_search_results()

    assert "Lace Top For Women" in result
    print(result) 