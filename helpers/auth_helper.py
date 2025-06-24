import os
from dotenv import load_dotenv
from app_manager import app

load_dotenv('.env.credentials')
user = os.getenv('USER_NAME')
blocked_user = os.getenv('BLOCKED_USER')
password = os.getenv('PASSWORD')


def success_login():
    app.login_page.open_login_page()
    app.login_page.fill_user_name(user)
    app.login_page.fill_password(password)
    app.login_page.press_login_button()