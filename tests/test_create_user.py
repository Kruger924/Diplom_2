import pytest
import allure
import requests

from data.urls import Urls, Handlers
from data.user_data import User


@allure.suite('Создание пользователя')
class TestCreateUser:

    @allure.description('Создание нового пользователя')
    @allure.title('Успешное создание нового пользователя')
    def test_create_new_user_success(self):
        user_data = User.create_data_user()
        with allure.step(f"Создание пользователя с данными: {user_data}"):
            response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=user_data)
        with allure.step(f"Проверка успешного создания пользователя (статус 200)"):
            assert response.status_code == 200 and response.json()["success"] is True

    @allure.description('При создании дублирующего пользователя возникает ответ 403 User already exists')
    @allure.title('Повторное создание существующего пользователя')
    def test_create_double_user_error(self, create_user):
        response_create, user_data, login_data, token = create_user
        
        with allure.step(f"Попытка создания дублирующего пользователя с данными: {user_data}"):
            response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=user_data)
        
        with allure.step("Проверка получения ошибки 403 с сообщением 'User already exists'"):
            allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)
            allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)
            assert response.status_code == 403 and 'User already exists' in response.text

    @allure.description('При создании пользователя с некорректными данными возникает ответ 403 Email, password and name are required fields')
    @allure.title('Создание пользователя с некорректными данными/ с незаполненными обязательными полями')
    @pytest.mark.parametrize("user_data, field_name", [
        (User.data_without_email, "без Email"),
        (User.data_without_password, "без Password"),
        (User.data_without_name, "без Name")
    ])
    def test_create_user_incorrect_data(self, user_data, field_name):
        with allure.step(f"Создание пользователя с некорректными данными ({field_name}): {user_data}"):
            response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=user_data)
        with allure.step("Проверка получения ошибки 403 с сообщением о необходимости заполнить все поля"):
            allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)
            allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)
            assert response.status_code == 403 and 'Email, password and name are required fields' in response.text