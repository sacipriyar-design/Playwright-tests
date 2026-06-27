from playwright.sync_api import sync_playwright
import csv

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False,slow_mo=1000)
    page=browser.new_page()
    page.goto("https://www.demoblaze.com/")
    #page.click("#signin2")
    
    #page.fill("#sign-username","testuser1")
    #page.fill("#sign-password","Password123")
    
    users=[
        ["PyT1", "Password123"],
        ["PyT2", "Password123"],
        ["PyT3", "Password123"]
    ]

    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        #writer.writerow(["Username", "Password"])
        page.on("dialog", lambda dialog: print(f"Dialog message: {dialog.message}") or dialog.accept())
    
        for user in users:
            username=user[0]
            password=user[1]
            page.goto("https://www.demoblaze.com/")
            page.click("#signin2")
            
            page.fill("#sign-username", username)
            page.fill("#sign-password", password)
            
            page.click("button[onclick='register()']")
            page.wait_for_timeout(3000)
            writer.writerow([username, password])
            print(f"Registered user: {username}")
            #page.click("button[class='btn btn-secondary']")  # Close the success dialog