from project_with_ui_autotests.pages.login_page import LoginPage
from project_with_ui_autotests.pages.product_catalog_page import CatalogPage
from project_with_ui_autotests.pages.cart_page import CartPage


class AppManager:
    def __init__(self):
        self.catalog_page = CatalogPage()
        self.login_page = LoginPage()
        self.cart_page = CartPage()

app = AppManager()