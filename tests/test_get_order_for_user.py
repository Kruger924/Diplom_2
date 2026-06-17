import allure
import requests

from data.urls import Urls, Handlers
from data.ingredients_data import Ingredient


@allure.suite("Получение доступных заказов по пользователю")
class TestGetOrderUser:

    @allure.description("")
    @allure.title("Успешное получение доступных заказов авторизованного пользователя")
    def test_get_order_user_with_auth(self, create_user):
        token = {'Authorization': create_user[3]}
        requests_create_order = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_ORDER}", headers=token, data=Ingredient.correct_ingredients_data)
        response_get_order = requests.get(f"{Urls.MAIN_URL}{Handlers.GET_ORDERS}", headers=token)
        assert response_get_order.status_code == 200 and response_get_order.json()['orders'][0]['number'] == requests_create_order.json()['order']['number']


    @allure.description("")
    @allure.title("Получение заказов пользователя не авторизованного пользователя выдает ответ 401")
    def test_get_order_user_not_auth(self):
        r = requests.get(f"{Urls.MAIN_URL}{Handlers.GET_ORDERS}")
        assert r.status_code == 401 and r.json()['message'] == "You should be authorised"