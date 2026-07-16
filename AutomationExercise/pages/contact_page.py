from playwright.sync_api import sync_playwright
import pytest


class ContactPage:
    def __init__(self, page, accept_dialog=True):
        self.page = page
        self.accept_dialog = accept_dialog
        self.dialog_message = None
        self.page.on("dialog", lambda dialog: self._handle_dialog(dialog))
        self.name_input = page.locator('[data-qa="name"]')
        self.email_input = page.locator('[data-qa="email"]')
        self.subject_input = page.locator('[data-qa="subject"]')
        self.message_input = page.locator('[data-qa="message"]')
        self.upload_file = page.locator('input[name="upload_file"]')
        self.submit_button = page.locator('[data-qa="submit-button"]')
        self.success_message = page.locator('.status.alert.alert-success')
        self.home_link = page.locator('a.btn.btn-success')

    def _handle_dialog(self, dialog):
        self.dialog_message = dialog.message
        if self.accept_dialog:
            dialog.accept()
        else:
            dialog.dismiss()

    def fill_name(self, name):
        self.name_input.fill(name)

    def fill_email(self, email):
        self.email_input.fill(email)

    def fill_subject(self, subject):
        self.subject_input.fill(subject)

    def fill_message(self, message):
        self.message_input.fill(message)

    def upload_attachment(self, file_path):
        self.upload_file.set_input_files(file_path)

    def click_submit(self):
        self.submit_button.click()

    def fill_all_fields(self, name, email,
                         subject, message):
        if name is not None:
            self.fill_name(name)
        if email is not None:
            self.fill_email(email)
        if subject is not None:
            self.fill_subject(subject)
        if message is not None:
            self.fill_message(message)