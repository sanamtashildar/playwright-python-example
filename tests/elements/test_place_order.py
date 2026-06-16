from playwright.sync_api import expect

from pages.LoginPage import LoginPage


def test_place_order(set_up_tear_down) -> None:
    """
    Verify that user is able to place an order successfully
    """
    page = set_up_tear_down
    credentials = {"username": "standard_user", "password": "secret_sauce"}
    login_p = LoginPage(page)
    products_p = login_p.login(credentials["username"], credentials["password"])

    product_name = "Sauce Labs Fleece Jacket"
    checkout_p = (
        products_p.click_add_to_cart_or_remove(product_name)
        .click_cart_icon()
        .click_checkout_button()
        .enter_checkout_information("Fn12", "Ln12", "0011")
        .click_continue()
        .click_finish_button()
    )

    expect(checkout_p.get_confirm_message()).to_have_text("Thank you for your order!")
