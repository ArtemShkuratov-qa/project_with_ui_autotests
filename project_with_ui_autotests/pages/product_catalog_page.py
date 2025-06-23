import allure
from selene import browser, be, have
from data.products import Product


class CatalogPage:

    @allure.step('Добавляем товар в корзину из каталога')
    def add_item_to_cart(self, product: Product):
        browser.element(product.add_id).click()

    @allure.step('Удаляем товар из корзины с страницы каталога')
    def remove_item_from_cart(self, product: Product):
        browser.element(product.remove_id).click()

    @allure.step('Проверяем отображение кнопки')
    def check_button_visibility(self, button_id):
        browser.element(button_id).should(be.visible)

    @allure.step('Проверяем количество товара по счетчику корзины')
    def check_quantity_in_cart(self, value):
        browser.element('[data-test="shopping-cart-badge"]').should(have.text(value))

    @allure.step('Проверяем отображение счетчика корзины')
    def check_quantity_icon_in_cart(self):
        browser.element('[data-test="shopping-cart-badge"]').should(be.hidden)

    @allure.step('Добавение товара в корзину через карточку товара')
    def add_item_to_cart_from_product_page(self, product: Product):
        target_item = browser.all('.inventory_item_name').by(have.exact_text(product.name))

        target_item.first.click()
        browser.element('#add-to-cart').click()

    @allure.step('Проверяем отображение кнопки "Remove" после добавления товара в корзину')
    def check_button_remove_on_product_page(self):
        browser.element('#remove').should(be.visible)
