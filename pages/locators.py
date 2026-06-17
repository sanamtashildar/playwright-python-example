"""
Locators for all page objects
Each page has its own locator class with all the selectors used on that page
"""


class LoginPageLocators:
    """Locators for Login Page"""

    USERNAME = "//input[@data-test='username']"  # or use get_by_placeholder("Username")
    PASSWORD = "//input[@data-test='password']"  # or use get_by_placeholder("Password")
    LOGIN_BUTTON = "//input[@id='login-button']"  # or use get_by_text("Login")
    ERROR_MESSAGE = "//h3[@data-test='error']"


class ProductListPageLocators:
    """Locators for Product List Page"""

    PRODUCTS_HEADER = "span.title"
    BURGER_MENU_BUTTON = "button#react-burger-menu-btn"
    LOGOUT_BUTTON = "#logout_sidebar_link"
    ADD_TO_CART_BUTTON = "//div[text()='Sauce Labs Bike Light']/ancestor::div[@class='inventory_item_label']/following-sibling::div//button"
    CART_ICON = "a.shopping_cart_link"
    ADD_REMOVE_CART_BUTTON_TEMPLATE = "//div[text()='{product}']/ancestor::div[@class='inventory_item_label']/following-sibling::div//button"


class CartPageLocators:
    """Locators for Cart Page"""

    CHECKOUT_BUTTON = "#checkout"


class CheckoutPageLocators:
    """Locators for Checkout Page"""

    FIRST_NAME = "[data-test='firstName']"
    LAST_NAME = "[data-test='lastName']"
    POSTAL_CODE = "[data-test='postalCode']"
    CONTINUE_BUTTON = "#continue"
    FINISH_BUTTON = "#finish"
    CONFIRM_MESSAGE = "h2.complete-header"
