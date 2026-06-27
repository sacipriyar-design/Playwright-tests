from pages.DemoSignupPage import DemoSignupPage
from pages.demo_login_page import DemoLoginPage
from playwright.sync_api import sync_playwright
import csv
import pytest

def test_demo_signup(test_goto_page):
    username="PYT15"
    password="password123"
    demo_signup=DemoSignupPage(test_goto_page)
    demo_signup.goto_homepage()
    demo_signup.signup_page(username,password)
    assert demo_signup.is_signup_succesful()

    login_page=DemoLoginPage(test_goto_page)
    login_page.goto_homepage()
    login_page.login(username,password)
    assert login_page.is_logged_in()



