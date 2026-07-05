from playwright.sync_api import sync_playwright
import pytest
class paymentpage:

    def __init__(self,page):
        self.page=page
        self.dialog_message=None
        self.page.on("dialog",lambda dialog: self._handle_dialog(dialog))

    def _handle_dialog(self,dialog):
        self.dialog_message=dialog.message
        dialog.close()

    def proceed_checkout(self):
        
        self.page.get_by_text("Proceed To Checkout").click()
        self.page.wait_for_url("**/checkout**")
        self.page.get_by_text("Place Order").click()
        self.page.wait_for_url("**/payment**",wait_until="commit")
    
    

    def payment_page(self,name,cardnumber,cvc,mm,yyyy):
        self.page.fill("[data-qa='name-on-card']", name)
        self.page.fill("[data-qa='card-number']", cardnumber)
        self.page.fill("[data-qa='cvc']", cvc)
        self.page.fill("[data-qa='expiry-month']",mm)
        self.page.fill("[data-qa='expiry-year']", yyyy)
        self.page.click("[data-qa='pay-button']")
        

