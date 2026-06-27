from playwright.sync_api import sync_playwright
import csv
from pages.demo_login_page import DemoLoginPage
import pytest

#Launchin the browser
@pytest.fixture
def test_goto_page():
    
    with sync_playwright() as p:
        Browser = p.chromium.launch(headless=False, slow_mo=1000)
        page =Browser.new_page()
        yield page
        Browser.close()
#read from csv file
def load_users():
    with open("users.csv","r") as file:
        reader=csv.DictReader(file)
       
        return [(row['Username'],row['Password'],row['Expected']) for row in reader]
#looping through pytest parameterize to read from csv file
@pytest.mark.parametrize("username,password,expected",load_users())
def test_login(test_goto_page,username,password,expected):
    
    Login_page=DemoLoginPage(test_goto_page)
    Login_page.goto_homepage()
    Login_page.login(username,password)
    if expected == 'pass':
        assert Login_page.is_logged_in() == True
        Login_page.logout()
    else:
        assert Login_page.get_error_message()