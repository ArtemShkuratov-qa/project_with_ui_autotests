import allure
from selene import browser, be, have
from data.clients import Client
from data.products import Product


class CartPage:

    @allure.step('Выполняем переход в корзину')
    def move_to_cart(self):
        browser.element('#shopping_cart_container').click()

    @allure.step('Выполняем переход к оформлению заказа')
    def move_to_checkout(self):
        browser.element('#checkout').click()

    @allure.step('Заполняем информацию о получателе')
    def fill_information_for_checkout(self, client: Client):
        browser.element('#first-name').type(client.first_name)
        browser.element('#last-name').type(client.last_name)
        browser.element('#postal-code').type(client.postal_code)

    @allure.step('Переходим на страницу подтверждения заказа')
    def continue_making_an_order(self):
        browser.element('#continue').click()

    @allure.step('Проверяем финальную стоимость позиции из заказа')
    def check_the_order_price(self, product: Product):
        browser.element('[data-test="subtotal-label"]').should(have.text(product.price))

    @allure.step('Завершаем оформление заказа')
    def click_on_the_finish_button(self):
        browser.element('#finish').click()

    @allure.step('Проверяем отображение баннера об успешном оформлении заказа')
    def check_complete_header(self):
        browser.element('[data-test="complete-header"]').should(have.exact_text('Thank you for your order!'))

    @allure.step('Проверяем отображение кнопки "Back Home" после успешного оформления заказа')
    def check_back_home_button(self):
        browser.element('#back-to-products').should(be.visible)

    @allure.step('Выполняем клик по кнопке "Back Home"')
    def click_on_back_home_button(self):
        browser.element('#back-to-products').click()

    @allure.step('Проверяем отсутствие товаров в корзине')
    def check_items_in_cart(self):
        browser.all('[data-test="inventory-item"]').should(be.hidden)

    @allure.step('Выполняем возврат к каталогу товаров из корзины')
    def move_to_catalog_from_cart(self):
        browser.element('#continue-shopping').click()

    @allure.step('Проверяем, что пользователь находится на странице каталога')
    def check_title_from_catalog_page(self):
        browser.element('[data-test="title"]').should(have.exact_text('Products'))
