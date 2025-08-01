import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"

@pytest.fixture
def logged_in_browser(browser):
    login = LoginPage(browser)
    login.navigate()
    login.login(VALID_USER, VALID_PASSWORD)
    return browser

def test_carregamento_dos_produtos(logged_in_browser):
    page = ProductsPage(logged_in_browser)
    assert page.inventory_items.count() == 6  # saucedemo sempre exibe 6 produtos

def test_ordenacao_nome_az(logged_in_browser):
    page = ProductsPage(logged_in_browser)
    page.select_sort_option("az")
    nomes = page.get_product_names()
    assert nomes == sorted(nomes)

def test_ordenacao_nome_za(logged_in_browser):
    page = ProductsPage(logged_in_browser)
    page.select_sort_option("za")
    nomes = page.get_product_names()
    assert nomes == sorted(nomes, reverse=True)

def test_ordenacao_preco_baixo_alto(logged_in_browser):
    page = ProductsPage(logged_in_browser)
    page.select_sort_option("lohi")
    precos = page.get_product_prices()
    assert precos == sorted(precos)

def test_ordenacao_preco_alto_baixo(logged_in_browser):
    page = ProductsPage(logged_in_browser)
    page.select_sort_option("hilo")
    precos = page.get_product_prices()
    assert precos == sorted(precos, reverse=True)

def test_adicao_de_itens_ao_carrinho(logged_in_browser):
    page = ProductsPage(logged_in_browser)
    page.add_to_cart_by_index(0)
    page.add_to_cart_by_index(1)
    assert page.get_cart_count() == "2"

def test_remocao_de_itens_do_carrinho(logged_in_browser):
    page = ProductsPage(logged_in_browser)
    page.add_to_cart_by_index(0)
    page.add_to_cart_by_index(1)
    page.remove_from_cart_by_index(0)
    assert page.get_cart_count() == "1"
