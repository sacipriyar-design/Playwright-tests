from playwright.sync_api import sync_playwright
import csv

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False,slow_mo=1000)
    page=browser.new_page()
    page.goto("https://www.demoblaze.com/")
    with open('users.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            username = row['Username']
            password = row['Password']

            page.goto("https://www.demoblaze.com/")
            page.wait_for_timeout(2000)
            page.click("#login2")
            page.wait_for_timeout(1000)
            page.fill("#loginusername", username)
            page.fill("#loginpassword", password)
    
            #page.click("button[onclick='logIn()']")
            page.click("button:has-text('Log in')")
            page.wait_for_timeout(3000)
            print(f"Current URL: {page.url}")
            print(f"nameofuser visible: {page.locator('#nameofuser').is_visible()}")
    # Check if login was successful
            if page.locator("#nameofuser").is_visible():
                print(f"Login successful for user: {username}")
                page.wait_for_timeout(2000)
                page.click("#logout2")  # Log out after successful login
            else:
                print(f"Login failed for user: {username}")