class MenuPage:
    def __init__(self, page):
        self.page = page
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")
        self.about_link = page.locator("#about_sidebar_link")
        self.reset_app_state_link = page.locator("#reset_sidebar_link")
        self.close_menu_button = page.locator("#react-burger-cross-btn")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def open_menu(self):
        self.menu_button.click()

    def logout(self):
        self.open_menu()
        self.logout_link.click()

    def go_to_about(self):
        self.open_menu()
        self.about_link.click()

    def reset_app_state(self):
        self.open_menu()
        self.reset_app_state_link.click()

    def is_cart_empty(self):
        return not self.cart_badge.is_visible()
