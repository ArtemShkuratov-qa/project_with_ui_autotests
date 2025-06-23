import allure
from selene import browser, be, have


class LoginPage:

    @allure.step('Открытие страницы авторизации')
    def open_login_page(self):
        browser.open('/')

    @allure.step('Вводим имя пользователя')
    def fill_user_name(self, value):
        browser.element('#user-name').type(value)

    @allure.step('Вводим пароль')
    def fill_password(self, value):
        browser.element('#password').type(value)

    @allure.step('Выполняем нажатие на кнопку "Login"')
    def press_login_button(self):
        browser.element('#login-button').click()

    @allure.step('Проверяем отображение иконки корзины после успешной авторизации')
    def check_shopping_cart(self):
        browser.element('.shopping_cart_container').should(be.visible)

    @allure.step('Проверяем отображение текстовой ошибки при неуспешной авторизации')
    def check_error_text(self, value):
        browser.element('[data-test=error]').should(
        have.exact_text(value))
