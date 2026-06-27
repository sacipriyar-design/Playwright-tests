class DemoLoginPage:
    def __init__(self,page):
        self.page=page
        self.dialog_message = None
        self.page.on("dialog",lambda dialog: self.handle_dialog(dialog))
    
    def handle_dialog(self,dialog):
        self.dialog_message = dialog.message
        dialog.accept()
    
    def goto_homepage(self):
        self.page.goto("https://www.demoblaze.com/")

    def login(self,username,password):
        self.page.click("#login2")
        self.page.wait_for_timeout(1000)
        self.page.fill("#loginusername", username)
        self.page.fill("#loginpassword", password)
        self.page.click("button:has-text('Log in')")
        
        self.page.wait_for_timeout(3000)
    
    def get_error_message(self):
        return self.dialog_message
    
    def is_logged_in(self):
        self.page.wait_for_timeout(3000)
        return self.page.locator("#nameofuser").is_visible() == True
    def logout(self):    
        self.page.click("#logout2")