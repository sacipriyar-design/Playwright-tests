from pages.cart_page import cartpage
import csv
import pytest

def test_cart(test_goto_page):
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
    cart.Logout()


def test_cart_without_Login(test_goto_page):
    test_goto_page.goto("https://automationexercise.com/products")
    cart=cartpage(test_goto_page)
    cart.page.wait_for_timeout(3000)

    cart.navigate_to_products()
    cart.search_product("Men Tshirt")
    cart.add_to_cart()
    cart.view_cart()
    assert "view_cart" in test_goto_page.url

def test_search_invalid(test_goto_page):
    test_goto_page.goto("https://automationexercise.com/products")
    cart=cartpage(test_goto_page)
    cart.page.wait_for_timeout(3000)
    cart.navigate_to_products()
    cart.search_product("xyzzzzzz")
    test_goto_page.wait_for_timeout(3000)
    products = test_goto_page.locator('[data-product-id]')
    assert products.count() == 0