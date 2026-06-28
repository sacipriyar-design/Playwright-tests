from playwright.sync_api import sync_playwright

class signup:
    def __init__(self,page):
        self.page=page
        self.dialog_message=None
        self.page.on("dialog",lambda dailog: self._handle_dialog())

    def _handle_dialog(self,dialog):
        dialog_message=dialog.message
        dialog.accept()
    
    def goto_page(self):
        self.page.goto("https://automationexercise.com/")

    def signup(self,name,email,title,password,day,month,year,firstname,lastname,company,address,address2,country,state,city,zipcode,mobilenumber):
        self.page.get_by_text("Signup / Login").click()
        self.page.wait_for_timeout(3000)
        #self.page.fill("#name",name)
        #self.page.fill("#email",email)
        self.page.fill("[data-qa='signup-name']", name)
        self.page.fill("[data-qa='signup-email']", email)
        self.page.locator("button",has_text="Signup").click()
        self.page.wait_for_timeout(3000)
        self.page.get_by_role("radio",name=title).check()
        self.page.fill("#password",password)
        self.page.wait_for_timeout(3000)
        self.page.select_option("#days",day)
        self.page.select_option("#months",month)
        self.page.select_option("#years",year)
        self.page.fill("#first_name",firstname)
        self.page.fill("#last_name",lastname)
        self.page.fill("#company",company)
        self.page.fill("#address1",address)
        self.page.fill("#address2",address2)
        self.page.select_option("#country",country)
        self.page.fill("#state",state)
        self.page.fill("#city",city)
        self.page.fill("#zipcode",zipcode)
        self.page.fill("#mobile_number",mobilenumber)
        self.page.locator("button",has_text="Create Account").click()
        self.page.wait_for_timeout(3000)

    def is_signup_successful(self):
        return "account_created" in  self.page.url