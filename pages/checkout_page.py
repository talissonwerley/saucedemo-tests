class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.cart_icon = page.locator(".shopping_cart_link")
        self.checkout_button = page.locator("#checkout")
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.cancel_button = page.locator("#cancel")
        self.success_message = page.locator(".complete-header")

    def go_to_cart(self):
        self.cart_icon.click()

    def start_checkout(self):
        self.checkout_button.click()

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    def finalize_purchase(self):
        self.finish_button.click()

    def cancel_purchase(self):
        self.cancel_button.click()

    def get_success_message(self):
        return self.success_message.inner_text()
