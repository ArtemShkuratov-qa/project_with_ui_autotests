import allure
from allure_commons.types import Severity

from app_manager import app
from helpers import auth_helper
from helpers.auth_helper import user
from helpers.auth_helper import blocked_user
from helpers.auth_helper import password


@allure.title('Успешная авторизация')
@allure.tag('web', 'smoke')
@allure.story('Авторизация')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Shkuratov Artem')
def test_authorization():
    auth_helper.success_login()

    app.login_page.check_shopping_cart()

@allure.title('Авторизация под заблокированным пользователем')
@allure.tag('web', 'smoke')
@allure.story('Авторизация')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Shkuratov Artem')
def test_authorization_with_blocked_user():
    app.login_page.open_login_page()

    app.login_page.fill_user_name(blocked_user)
    app.login_page.fill_password(password)
    app.login_page.press_login_button()

    app.login_page.check_error_text('Epic sadface: Sorry, this user has been locked out.')

@allure.title('Авторизация без ввода пароля')
@allure.tag('web', 'smoke')
@allure.story('Авторизация')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Shkuratov Artem')
def test_authorization_without_password():
    app.login_page.open_login_page()

    app.login_page.fill_user_name(user)
    app.login_page.press_login_button()

    app.login_page.check_error_text('Epic sadface: Password is required')