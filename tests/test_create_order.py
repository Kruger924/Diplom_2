import allure
import requests

from data.urls import Urls, Handlers
from data.ingredients_data import Ingredient


@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.description("Проверка создания заказа авторизованным пользователем с корректными ингредиентами")
    @allure.title("Успешное создание заказа авторизованным пользователем")
    def test_create_order_with_auth(self, create_user):
        with allure.step("Подготовка токена авторизации"):
            token = {'Authorization': create_user[3]}
        
        with allure.step(f"Отправка POST запроса на создание заказа с ингредиентами: {Ingredient.correct_ingredients_data}"):
            r = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_ORDER}", headers=token, data=Ingredient.correct_ingredients_data)
        
        with allure.step("Проверка успешного создания заказа"):
            assert r.status_code == 200 and r.json().get("success") is True

    @allure.description("Проверка создания заказа неавторизованным пользователем с корректными ингредиентами")
    @allure.title("Успешное создание заказа не авторизованным пользователем")
    def test_create_order_not_auth(self):
        with allure.step(f"Отправка POST запроса на создание заказа без токена с ингредиентами: {Ingredient.correct_ingredients_data}"):
            r = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_ORDER}", data=Ingredient.correct_ingredients_data)
        
        with allure.step("Проверка успешного создания заказа без авторизации"):
            assert r.status_code == 200 and r.json().get("success") is True

    @allure.description("Проверка создания заказа без указания ингредиентов")
    @allure.title("Создание заказа без ингредиентов выдает ответ 400")
    def test_create_order_without_ingredients(self):
        with allure.step("Отправка POST запроса на создание заказа без ингредиентов"):
            r = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_ORDER}")
        
        with allure.step("Проверка получения ошибки 400 с сообщением об отсутствии ингредиентов"):
            assert r.status_code == 400 and r.json()['message'] == "Ingredient ids must be provided"

    @allure.description("Проверка создания заказа с невалидным хешем ингредиента")
    @allure.title("Создание с невалидным хешем ингредиента выдает ответ 500")
    def test_create_order_invalid_hash_ingredient(self):
        with allure.step(f"Отправка POST запроса с невалидными данными ингредиентов: {Ingredient.incorrect_ingredients_data}"):
            response = requests.post(Urls.MAIN_URL + Handlers.CREATE_ORDER, 
                                    headers=Handlers.headers,
                                    json=Ingredient.incorrect_ingredients_data)
        
        with allure.step("Проверка получения ошибки 500 Internal Server Error"):
            assert response.status_code == 500 and 'Internal Server Error' in response.text