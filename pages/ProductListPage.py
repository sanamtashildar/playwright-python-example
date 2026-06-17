from pages.CartPage import CartPage
from pages.locators import ProductListPageLocators


class ProductListPage:

    def __init__(self, page):
        self.page = page

    def click_burger_menu_btn(self):
        """This will click on Burger menu icon from header"""
        self.page.locator(ProductListPageLocators.BURGER_MENU_BUTTON).click()
        return self

    def click_logout(self):
        """This will click on logout"""
        self.page.locator(ProductListPageLocators.LOGOUT_BUTTON).click()
        return self

    def do_logout(self):
        """Logout from the sauce demo"""
        self.click_burger_menu_btn()
        self.click_logout()

    def click_add_to_cart_or_remove(self, product):
        """ "This will click on add to cart or remove button for the given product name
        Args:
            product: Name of the product to add or remove from cart
        """
        self.page.locator(
            ProductListPageLocators.ADD_REMOVE_CART_BUTTON_TEMPLATE.format(
                product=product
            )
        ).click()
        return self

    def click_cart_icon(self):
        self.page.locator(ProductListPageLocators.CART_ICON).click()
        return CartPage(self.page)
