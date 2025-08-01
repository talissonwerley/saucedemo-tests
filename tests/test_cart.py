import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"

@pytest.fixture
def logged_in_with_items(browser):
    login = LoginPage(browser)
    login.navigate()
    login.login(VALID_USER, VALID_PASSWORD)
    
    products = ProductsPage(browser)
    products.add_to_cart_by_index(0)
    products.add_to_cart_by_index(1)

    cart = CartPage(browser)
    cart.go_to_cart()
    
    return browser

def test_acessar_carrinho_e_verificar_itens(logged_in_with_items):
    cart = CartPage(logged_in_with_items)
    assert cart.get_cart_items_count() == 2

def test_continuar_comprando_volta_para_pagina_de_produtos(logged_in_with_items):
    cart = CartPage(logged_in_with_items)
    cart.continue_shopping()
    assert "inventory.html" in logged_in_with_items.url

def test_remover_produto_do_carrinho(logged_in_with_items):
    cart = CartPage(logged_in_with_items)
    cart.remove_item_by_index(0)
    assert cart.get_cart_items_count() == 1
