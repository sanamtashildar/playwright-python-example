from playwright.sync_api import expect

from pages.checkout_data import CheckoutData
from pages.LoginPage import LoginPage


def test_e2e_checkout_login_add_to_cart_checkout_logout(set_up_tear_down):
    """Verify end-to-end workflow: login, add to cart, checkout, and logout."""
    page = set_up_tear_down
    username = "standard_user"
    password = "secret_sauce"

    login_page = LoginPage(page)
    product_page = login_page.login(username, password)

    product_name = "Sauce Labs Fleece Jacket"
    cart_page = product_page.click_add_to_cart_or_remove(product_name).click_cart_icon()

    checkout_page = cart_page.click_checkout_button()
    checkout_page.checkout(CheckoutData())

    expect(checkout_page.get_confirm_message()).to_have_text(
        "Thank you for your order!"
    )

    # Logout after checkout by returning to products page and using the burger menu logout flow
    product_page.click_burger_menu_btn()
    product_page.click_logout()
    expect(login_page.login_button).to_be_visible()
