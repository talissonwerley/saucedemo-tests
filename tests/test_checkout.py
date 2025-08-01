import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage

VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"

@pytest.fixture
def browser_with_cart(browser):
    login = LoginPage(browser)
    login.navigate()
    login.login(VALID_USER, VALID_PASSWORD)

    products = ProductsPage(browser)
    products.add_to_cart_by_index(0)

    checkout = CheckoutPage(browser)
    checkout.go_to_cart()
    checkout.start_checkout()

    return browser

def test_preencher_dados_de_envio(browser_with_cart):
    checkout = CheckoutPage(browser_with_cart)
    checkout.fill_checkout_info("Talisson", "Werley", "12345")
    assert "checkout-step-two.html" in browser_with_cart.url

def test_finalizar_compra(browser_with_cart):
    checkout = CheckoutPage(browser_with_cart)
    checkout.fill_checkout_info("Talisson", "Werley", "12345")
    checkout.finalize_purchase()
    assert "checkout-complete.html" in browser_with_cart.url
    assert "thank you" in checkout.get_success_message().lower()

def test_cancelar_compra(browser_with_cart):
    checkout = CheckoutPage(browser_with_cart)
    # preencher dados de envio (obrigatório para acessar o botão de cancelar na etapa 2)
    checkout.fill_checkout_info("Talisson", "Werley", "12345")
    # agora sim estamos na etapa 2 e o botão "cancel" está visível
    checkout.cancel_purchase()
    # deve voltar para a página de produtos
    assert "inventory.html" in browser_with_cart.url
