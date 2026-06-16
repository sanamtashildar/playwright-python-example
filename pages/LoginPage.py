from pages.ProductListPage import ProductListPage
from pages.locators import LoginPageLocators

class LoginPage:

    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        """
        Complete the login process in a single function
        
        Args:
            username: The username to login with
            password: The password to login with
        
        Returns:
            ProductListPage after successful login
        """
        self.page.locator(LoginPageLocators.USERNAME).clear()
        self.page.locator(LoginPageLocators.USERNAME).fill(username)
        self.page.locator(LoginPageLocators.PASSWORD).clear()
        self.page.locator(LoginPageLocators.PASSWORD).fill(password)
        self.page.locator(LoginPageLocators.LOGIN_BUTTON).click()
        return ProductListPage(self.page)

    @property
    def err_msg_loc(self):
        return self.page.locator(LoginPageLocators.ERROR_MESSAGE)

    @property
    def login_button(self):
        return self.page.locator(LoginPageLocators.LOGIN_BUTTON)
