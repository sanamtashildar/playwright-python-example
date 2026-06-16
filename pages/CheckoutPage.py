from pages.locators import CheckoutPageLocators
from pages.checkout_data import CheckoutData


class CheckoutPage:

    def __init__(self, page):
        self.page = page

    def get_confirm_message(self):
        return self.page.locator(CheckoutPageLocators.CONFIRM_MESSAGE)

    def checkout(self, checkout_data: CheckoutData):
        """
        Complete the checkout process with all steps in one function
        
        Args:
            checkout_data: Optional CheckoutData object with first_name, last_name, and postal_code.
                          If None, a new CheckoutData object will be generated.
        
        Returns:
            self for method chaining
        """
        if checkout_data is None:
            checkout_data = CheckoutData()
        
        self.page.locator(CheckoutPageLocators.FIRST_NAME).fill(checkout_data.first_name)
        self.page.locator(CheckoutPageLocators.LAST_NAME).fill(checkout_data.last_name)
        self.page.locator(CheckoutPageLocators.POSTAL_CODE).fill(checkout_data.postal_code)
        self.page.locator(CheckoutPageLocators.CONTINUE_BUTTON).click()
        self.page.locator(CheckoutPageLocators.FINISH_BUTTON).click()
        return self
