from src.automation_playwright.pages.CheckoutPage import CheckoutPage


class CartPage:
    """
    Doc strin
    """

    def __init__(self, page):
        self.page = page
        self._checkout_button = page.locator("#checkout")

    def click_checkout_button(self):
        self._checkout_button.click()
        return CheckoutPage(self.page)
