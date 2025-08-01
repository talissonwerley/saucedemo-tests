class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_items = page.locator(".cart_item")
        self.continue_shopping_button = page.locator("#continue-shopping")
        self.remove_buttons = page.locator("button:has-text('Remove')")

    def go_to_cart(self):
        self.cart_icon.click()

    def get_cart_items_count(self):
        return self.cart_items.count()

    def continue_shopping(self):
        self.continue_shopping_button.click()

    def remove_item_by_index(self, index):
        self.remove_buttons.nth(index).click()
