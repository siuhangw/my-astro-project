from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:4321/')
        page.wait_for_selector('footer a')

        # Hover over the github social link
        github_link = page.locator('footer a', has_text='github')
        github_link.hover()
        page.wait_for_timeout(500) # Wait for hover transition

        page.screenshot(path='social_hover.png')
        browser.close()

verify()
