import allure
import requests

from data.urls import Urls, Handlers
from data.user_data import User


@allure.suite('Авторизация пользователя')
class Testlogin:

    @allure.description('Успешная авторизация существующего пользователя')
    @allure.title('Авторизация существующего пользователя')
    def test_login_user(self, create_user):
        login_data = create_user[2]
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN}', data=login_data)
        assert response.status_code == 200 and response.json().get('success') is True

    @allure.description('Авторизация пользователя с некорректным логином/паролем возникает ответ 401')
    @allure.title('Авторизация с некорректным логином/паролем')
    def test_login_user_error(self):
        payload = User.create_data_user()
        login_data = payload.copy()
        login_data['password'] = 'wrong_password'
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN}', data=login_data)
        assert response.status_code == 401 and response.json().get('success') is False