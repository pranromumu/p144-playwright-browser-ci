from playwright.sync_api import sync_playwright
def test_playwright_browser_ci():
    with sync_playwright()as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/")
        assert "The Internet" in page.title()
        browser.close()
