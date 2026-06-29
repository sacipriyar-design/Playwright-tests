from playwright.sync_api import sync_playwright
class LoginPage:
    def __init__(self,page):
        self.page=page
        self.dialog_message=None
        self.page.on("dialog",lambda dialog:self._handle_dialog(dialog))

    def _handle_dialog(self,dialog):
        self.dialog_message=dialog.message
        dialog.accept()

    def goto_page(self):
        self.page.goto("https://automationexercise.com/")

    def login(self,email,password):
        self.page.get_by_text("Signup / Login").click()
        self.page.fill("[data-qa='login-email']",email)
        self.page.fill("[data-qa='login-password']",password)
        self.page.locator("button",has_text="Login").click()
        self.page.wait_for_timeout(3000)
    
    def is_login_successful(self):
       return self.page.locator("#loggedInUser").is_visible()

    def Logout(self):
        self.page.get_by_text("Logout").click()