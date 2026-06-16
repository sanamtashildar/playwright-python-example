from pages.CheckoutPage import CheckoutPage
from pages.locators import CartPageLocators


class CartPage:
    """
    Doc strin
    """

    def __init__(self, page):
        self.page = page
        self._checkout_button = page.locator(CartPageLocators.CHECKOUT_BUTTON)

    def click_checkout_button(self):
        self._checkout_button.click()
        return CheckoutPage(self.page)
