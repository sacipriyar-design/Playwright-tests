from pages.DemoSignupPage import DemoSignupPage
from playwright.sync_api import sync_playwright
import csv
import pytest
users=[
    ["PyT11", "Password123"],
    ["PyT12", "Password123"],
    ["PyT13", "Password123"]
    ]   
        
@pytest.mark.parametrize("username,password",users)
def test_signup(test_goto_page,username,password):
    signup_page=DemoSignupPage(test_goto_page)
    signup_page.goto_homepage()
    signup_page.signup_page(username,password)
    assert signup_page.is_signup_succesful()
    with open("usersT.csv","a", newline='') as file:
        writer=csv.writer(file)
        writer.writerow([username,password])

