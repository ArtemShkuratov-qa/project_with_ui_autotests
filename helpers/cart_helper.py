from app_manager import app
from data.clients import Client
from data.products import Product
from helpers import auth_helper


def making_an_order(product: Product, client: Client):
    auth_helper.success_login()
    app.catalog_page.add_item_to_cart_from_product_page(product)
    app.cart_page.move_to_cart()
    app.cart_page.move_to_checkout()
    app.cart_page.fill_information_for_checkout(client)
    app.cart_page.continue_making_an_order()
    app.cart_page.check_the_order_price(product)
    app.cart_page.click_on_the_finish_button()