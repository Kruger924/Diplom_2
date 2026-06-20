import allure
import requests

from data.urls import Urls, Handlers
from data.user_data import User


@allure.suite('Изменение данных пользовователя')
class TestChangingUserData:

    @allure.description("Замена email у авторизованного пользователя происходит успешно")
    @allure.title("Успешное изменение email авторизованного пользователя")
    def test_changing_user_email_with_auth(self, create_user):
        with allure.step("Подготовка тестовых данных"):
            payload = {'email': User.create_data_user()["email"]}
            token = {'Authorization': create_user[3]}
        
        with allure.step(f"Отправка PATCH запроса на изменение email на {payload['email']}"):
            r = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_DATA}", headers=token, data=payload)
        
        with allure.step("Проверка ответа сервера"):
            assert r.status_code == 200 and r.json()['user']['email'] == payload["email"]

    @allure.description("Замена пароля у авторизованного пользователя происходит успешно")
    @allure.title("Успешное изменение password авторизованного пользователя")
    def test_changing_user_password_with_auth(self, create_user):
        with allure.step("Подготовка тестовых данных"):
            payload = {'password': User.create_data_user()["password"]}
            token = {'Authorization': create_user[3]}
        
        with allure.step("Отправка PATCH запроса на изменение пароля"):
            r = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_DATA}", headers=token, data=payload)
        
        with allure.step("Проверка ответа сервера"):
            assert r.status_code == 200 and r.json().get("success") is True

    @allure.description("Замена имени у авторизованного пользователя происходит успешно")
    @allure.title("Успешное изменение name авторизованного пользователя")
    def test_changing_user_name_with_auth(self, create_user):
        with allure.step("Подготовка тестовых данных"):
            payload = {'name': User.create_data_user()["name"]}
            token = {'Authorization': create_user[3]}
        
        with allure.step(f"Отправка PATCH запроса на изменение имени на {payload['name']}"):
            r = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_DATA}", headers=token, data=payload)
        
        with allure.step("Проверка ответа сервера"):
            assert r.status_code == 200 and r.json()['user']['name'] == payload["name"]

    @allure.description("Изменение даных пользователя без авторизации выдает ответ 401")
    @allure.title("Изменение данных пользователя без авторизацией")
    def test_changing_user_data_not_auth(self):
        with allure.step("Подготовка тестовых данных"):
            test_data = User.create_data_user()
        
        with allure.step("Отправка PATCH запроса без токена авторизации"):
            r = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_DATA}", data=test_data)
        
        with allure.step("Проверка ответа сервера"):
            assert r.status_code == 401 and r.json()['message'] == 'You should be authorised'