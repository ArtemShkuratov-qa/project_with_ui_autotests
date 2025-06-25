import allure
from allure_commons.types import Severity

from app_manager import app
from data import products
from helpers import auth_helper
from data import clients
from helpers import cart_helper


@allure.title('Оформление заказа')
@allure.tag('web', 'smoke')
@allure.story('Оформление заказа')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Shkuratov Artem')
def test_place_order():
    cart_helper.making_an_order(products.bike_light, clients.test_user1)
    app.cart_page.check_complete_header()
    app.cart_page.check_back_home_button()

@allure.title('Возврат к каталогу товаров из корзины')
@allure.tag('web', 'smoke')
@allure.story('Корзина')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Shkuratov Artem')
def test_return_to_catalog_from_cart():
    auth_helper.success_login()
    app.cart_page.move_to_cart()
    app.cart_page.move_to_catalog_from_cart()
    app.cart_page.check_title_from_catalog_page()

@allure.title('Удаление товара из корзины')
@allure.tag('web', 'smoke')
@allure.story('Корзина')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Shkuratov Artem')
def test_remove_item_from_cart():
    auth_helper.success_login()
    app.catalog_page.add_item_to_cart(products.fleece_jacket)
    app.cart_page.move_to_cart()
    app.catalog_page.remove_item_from_cart(products.fleece_jacket)
    app.cart_page.check_items_in_cart()

@allure.title('Возврат к каталогу с товарами после успешного оформления заказа')
@allure.tag('web', 'smoke')
@allure.story('Оформление заказа')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Shkuratov Artem')
def test_return_to_catalog():
    cart_helper.making_an_order(products.fleece_jacket, clients.test_user2)
    app.cart_page.click_on_back_home_button()
    app.cart_page.check_title_from_catalog_page()