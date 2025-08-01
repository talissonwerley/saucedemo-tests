import pytest
from pages.login_page import LoginPage

# Credenciais padrão do site
VALID_USER = "standard_user"
BLOCKED_USER = "locked_out_user"
VALID_PASSWORD = "secret_sauce"
INVALID_PASSWORD = "wrongpass"

def test_login_valido(browser):
    login = LoginPage(browser)
    login.navigate()
    login.login(VALID_USER, VALID_PASSWORD)
    assert browser.url == "https://www.saucedemo.com/inventory.html"

def test_login_usuario_bloqueado(browser):
    login = LoginPage(browser)
    login.navigate()
    login.login(BLOCKED_USER, VALID_PASSWORD)
    assert login.error_message.is_visible()
    assert "locked out" in login.get_error_text().lower()

def test_login_campos_vazios(browser):
    login = LoginPage(browser)
    login.navigate()
    login.login("", "")
    assert login.error_message.is_visible()
    assert "username is required" in login.get_error_text().lower()

def test_login_senha_incorreta(browser):
    login = LoginPage(browser)
    login.navigate()
    login.login(VALID_USER, INVALID_PASSWORD)
    assert login.error_message.is_visible()
    assert "do not match" in login.get_error_text().lower()
