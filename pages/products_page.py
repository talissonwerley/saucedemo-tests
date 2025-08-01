class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.inventory_items = page.locator(".inventory_item")
        self.sort_dropdown = page.locator(".product_sort_container")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def get_product_names(self):
        return self.page.locator(".inventory_item_name").all_text_contents()

    def get_product_prices(self):
        prices = self.page.locator(".inventory_item_price").all_text_contents()
        return [float(p.replace("$", "")) for p in prices]

    def select_sort_option(self, value):
        self.sort_dropdown.select_option(value)

    def add_to_cart_by_index(self, index):
        self.page.locator("button:has-text('Add to cart')").nth(index).click()

    def remove_from_cart_by_index(self, index):
        self.page.locator("button:has-text('Remove')").nth(index).click()

    def get_cart_count(self):
        return self.cart_badge.inner_text() if self.cart_badge.is_visible() else "0"
