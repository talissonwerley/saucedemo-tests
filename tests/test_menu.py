import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.menu_page import MenuPage

VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"

@pytest.fixture
def logged_in_browser(browser):
    login = LoginPage(browser)
    login.navigate()
    login.login(VALID_USER, VALID_PASSWORD)
    return browser

def test_logout(logged_in_browser):
    menu = MenuPage(logged_in_browser)
    menu.logout()
    # Aguardamos o redirecionamento e garantimos que a URL é de login
    logged_in_browser.wait_for_url("**/")
    # Validar que voltamos para a tela de login
    assert "saucedemo.com" in logged_in_browser.url
    assert logged_in_browser.locator("input[name='user-name']").is_visible()
    assert logged_in_browser.locator("input[name='password']").is_visible()

def test_acessar_about(logged_in_browser):
    menu = MenuPage(logged_in_browser)
    menu.go_to_about()
    assert "saucelabs.com" in logged_in_browser.url

def test_reset_app_state(logged_in_browser):
    products = ProductsPage(logged_in_browser)
    products.add_to_cart_by_index(0)

    menu = MenuPage(logged_in_browser)
    menu.reset_app_state()
    assert menu.is_cart_empty()
