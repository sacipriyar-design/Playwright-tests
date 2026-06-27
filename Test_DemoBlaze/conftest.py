from playwright.sync_api import sync_playwright
import pytest
@pytest.fixture

def test_goto_page():
    with sync_playwright() as p:
        Browser = p.chromium.launch(headless=True)
        page=Browser.new_page()
        yield page
        Browser.close()
