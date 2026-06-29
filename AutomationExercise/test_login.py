from pages.login_page import LoginPage
import pytest
import csv

def load_user():
    with open("users.csv","r") as file:
        reader=csv.DictReader(file)
        return [(row['email'],row['password'])for row in reader]

@pytest.mark.parametrize("email,password",load_user())
def test_login(test_goto_page,email,password):
    login_page=LoginPage(test_goto_page)
    login_page.goto_page()
    login_page.login(email,password)
    login_page.is_login_successful()
    login_page.Logout()
