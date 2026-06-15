from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Aici definim toți locatorii într-un singur loc sigur
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator("#flash")

    def navigheaza(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()