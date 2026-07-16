from pages.cart_page import cartpage
import csv
import pytest
from playwright.sync_api import expect
import re

def test_cart(cart_page_login):
    cart_page_login.search_product("Men Tshirt")
    expect(cart_page_login.page.locator(".product-image-wrapper").first).to_be_visible()
    cart_page_login.add_to_cart()
    cart_page_login.view_cart()
    expect(cart_page_login.page).to_have_url(re.compile("view_cart"))
    cart_page_login.Logout()


def test_cart_without_Login(test_goto_page):
    test_goto_page.goto("https://automationexercise.com/products")
    cart=cartpage(test_goto_page)
    expect(test_goto_page.get_by_text(" Products")).to_be_visible()

    cart.navigate_to_products()
    cart.search_product("Men Tshirt")
    cart.add_to_cart()
    cart.view_cart()
    assert "view_cart" in test_goto_page.url

def test_search_invalid(test_goto_page):
    test_goto_page.goto("https://automationexercise.com/products")
    cart=cartpage(test_goto_page)
    expect(test_goto_page.get_by_text(" Products")).to_be_visible()
    cart.navigate_to_products()
    cart.search_product("xyzzzzzz")
    expect(test_goto_page).to_have_url(re.compile("search=xyzzzzzzzzzzzzzzzzzz"))
    products = test_goto_page.locator('[data-product-id]')
    assert products.count() == 0 