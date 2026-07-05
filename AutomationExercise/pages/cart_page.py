from playwright.sync_api import sync_playwright
import pytest
class cartpage:
    def __init__(self,page):
        self.page=page
        self.dialog_message=None
        self.page.on("dialog",lambda dialog: self._handle_dialog(dialog))

    def _handle_dialog(self,dialog):
        self.dialog_message=dialog.message
        dialog.accept()

    def navigate_to_products(self):
        self.page.get_by_role("link", name=" Products").click()
    
    def search_product(self, product_name):
        self.page.fill("#search_product",product_name)
        self.page.click("#submit_search")  
    
    def add_to_cart(self):
        self.page.locator('[data-product-id="2"]').first.click()
    
    def view_cart(self):
        self.page.get_by_text("View Cart").click()
        

    def Logout(self):
        self.page.get_by_text(" Logout").click()
       

    def get_product_name(self):
        return self.page.locator(".product-image-wrapper .productinfo p").first.text_content()

    def get_all_search_results(self):
        self.page.locator(".product-image-wrapper .productinfo p").first.wait_for()
        return self.page.locator(".product-image-wrapper .productinfo p").all_text_contents()