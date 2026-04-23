from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:4321/')
        page.wait_for_selector('footer a')

        # Focus on the twitter social link using keyboard
        page.keyboard.press('Tab') # Skip link
        page.keyboard.press('Tab') # Theme toggle
        page.keyboard.press('Tab') # Menu
        page.keyboard.press('Tab') # Home
        page.keyboard.press('Tab') # About
        page.keyboard.press('Tab') # Blog
        page.keyboard.press('Tab') # New greeting
        page.keyboard.press('Tab') # Twitter

        page.wait_for_timeout(500) # Wait for focus transition

        page.screenshot(path='social_focus.png')
        browser.close()

verify()
