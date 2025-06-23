import allure
from allure_commons.types import Severity

from app_manager import app
from data import products
from helpers import auth_helper


@allure.title('Добавление товара в корзину через карточку товара')
@allure.tag('web', 'smoke')
@allure.story('Добавление товара в корзину')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Shkuratov Artem')
def test_add_item_to_cart_from_product_page():
    auth_helper.success_login()
    app.catalog_page.add_item_to_cart_from_product_page(products.bike_light)

    app.catalog_page.check_button_remove_on_product_page()
    app.catalog_page.check_quantity_in_cart('1')

@allure.title('Добавление товара в корзину через каталог')
@allure.tag('web', 'smoke')
@allure.story('Добавление товара в корзину')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Shkuratov Artem')
def test_add_items_to_cart_from_product_catalog():
    auth_helper.success_login()
    app.catalog_page.add_item_to_cart(products.t_shirt)
    app.catalog_page.add_item_to_cart(products.fleece_jacket)

    app.catalog_page.check_button_visibility(products.t_shirt.remove_id)
    app.catalog_page.check_button_visibility(products.fleece_jacket.remove_id)
    app.catalog_page.check_quantity_in_cart('2')

@allure.title('Удаление товара из корзины через каталог')
@allure.tag('web', 'smoke')
@allure.story('Удаление товара из корзины')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Shkuratov Artem')
def test_remove_item_from_cart():
    auth_helper.success_login()
    app.catalog_page.add_item_to_cart(products.bike_light)
    app.catalog_page.check_button_visibility(products.bike_light.remove_id)
    app.catalog_page.check_quantity_in_cart('1')
    app.catalog_page.remove_item_from_cart(products.bike_light)
    app.catalog_page.check_button_visibility(products.bike_light.add_id)
    app.catalog_page.check_quantity_icon_in_cart()
