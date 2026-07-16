from playwright.sync_api import expect, sync_playwright
import pytest
import re

def test_valid_contact_submit(contact_page):
    contact=contact_page
    contact.fill_all_fields("saci","test@gg.com","test","test")
    contact.click_submit()
    assert contact.dialog_message =="Press OK to proceed!"
    expect(contact_page.success_message).to_be_visible()


@pytest.mark.parametrize("invalid_email", ["", "www", "wwww@"])
def test_invalid_email_formats_blocked(contact_page, invalid_email):
    if invalid_email:
        contact_page.fill_name("saci")
        contact_page.fill_email(invalid_email)
        contact_page.fill_subject("test")
        contact_page.fill_message("test")
    contact_page.click_submit()
    
    is_valid = contact_page.email_input.evaluate("el => el.checkValidity()")
    assert is_valid is False
    expect(contact_page.success_message).not_to_be_visible()