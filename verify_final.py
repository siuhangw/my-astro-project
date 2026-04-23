from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:4321/')
        page.wait_for_selector('footer a')

        # Focus on the twitter social link using keyboard
        # It's better to hover, to make sure github gets the light purple color

        github_link = page.locator('footer a', has_text='Github')
        github_link.hover()

        page.wait_for_timeout(500) # Wait for focus transition

        page.screenshot(path='social_hover_capitalized.png')
        browser.close()

verify()
