class DemoSignupPage:
    def __init__(self,page):
        self.page=page
        self.dialog_message=None
        self.page.on("dialog", lambda dialog:self ._handle_dialog(dialog))
    
    def _handle_dialog(self,dialog):
        self.dialog_message = dialog.message
        dialog.accept()

    def goto_homepage(self):
        self.page.goto("https://www.demoblaze.com/")
    
    def signup_page(self,username,password):
        self.page.click("#signin2")

        self.page.fill("#sign-username",username)
        self.page.fill("#sign-password",password)
        self.page.click("button[onclick='register()']")
        self.page.wait_for_timeout(3000)

    def is_signup_succesful(self):
        return "Sign up successful" in self.dialog_message