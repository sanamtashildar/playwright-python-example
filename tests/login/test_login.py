from playwright.sync_api import Page, expect

from src.automation_playwright.pages.LoginPage import LoginPage


def test_login_with_standard_user(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {"username": "standard_user", "password": "secret_sauce"}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    expect(products_p.product_header).to_be_visible()
    expect(products_p.product_header).to_have_text("Products")


def test_login_with_invalid_user(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {"username": "nonstandard_user", "password": "secret_sauce"}
    login_p = LoginPage(page)
    login_p.do_login(credentials)
    expected_fail_message = (
        "Username and password do not match any user in this service"
    )
    expect(login_p.err_msg_loc).to_contain_text(expected_fail_message)


def test_login_with_no_credentials(set_up_tear_down) -> None:
    page = set_up_tear_down
    login_p = LoginPage(page)
    login_p.click_login()
    expected_fail_message = "Username is required"
    expect(login_p.err_msg_loc).to_contain_text(expected_fail_message)


def test_acces_inventory_without_login(set_up_tear_down) -> None:
    page = set_up_tear_down
    page.goto("https://www.saucedemo.com/inventory.html")
    login_p = LoginPage(page)
    expect(login_p.err_msg_loc).to_contain_text(
        "You can only access '/inventory.html' when you are logged in"
    )
