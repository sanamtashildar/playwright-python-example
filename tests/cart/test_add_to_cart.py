from playwright.sync_api import expect

from src.automation_playwright.pages.LoginPage import LoginPage


def test_add_to_cart(set_up_tear_down) -> None:
    """
    Verify that add to cart button is changed to Remove when clicked
    """
    page = set_up_tear_down
    credentials = {"username": "standard_user", "password": "secret_sauce"}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)

    product_name = "Sauce Labs Bolt T-Shirt"

    products_p.click_add_to_cart_or_remove(product_name)

    expect(products_p.get_add_remove_cart_locator(product_name)).to_have_text("Remove")


def test_remove_product_from_cart(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {"username": "standard_user", "password": "secret_sauce"}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)

    product_name = "Sauce Labs Bolt T-Shirt"

    products_p.click_add_to_cart_or_remove(product_name)

    products_p.click_add_to_cart_or_remove(product_name)

    expect(products_p.get_add_remove_cart_locator(product_name)).to_have_text(
        "Add to cart"
    )
