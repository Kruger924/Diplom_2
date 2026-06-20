import allure
import requests

from data.urls import Urls, Handlers
from data.ingredients_data import Ingredient


@allure.suite("Получение доступных заказов по пользователю")
class TestGetOrderUser:

    @allure.description("Проверка получения списка заказов авторизованным пользователем после создания заказа")
    @allure.title("Успешное получение доступных заказов авторизованного пользователя")
    def test_get_order_user_with_auth(self, create_user):
        token = {'Authorization': create_user[3]}
        
        with allure.step("Создание заказа авторизованным пользователем"):
            requests_create_order = requests.post(
                f"{Urls.MAIN_URL}{Handlers.CREATE_ORDER}", 
                headers=token, 
                data=Ingredient.correct_ingredients_data
            )
            allure.attach(requests_create_order.text, "Create Order Response", allure.attachment_type.JSON)
        
        with allure.step("Получение заказов авторизованного пользователя"):
            response_get_order = requests.get(f"{Urls.MAIN_URL}{Handlers.GET_ORDERS}", headers=token)
            allure.attach(response_get_order.text, "Get Orders Response", allure.attachment_type.JSON)
        
        with allure.step("Проверка соответствия созданного заказа и полученного из списка"):
            assert response_get_order.status_code == 200
            assert response_get_order.json()['orders'][0]['number'] == requests_create_order.json()['order']['number']

    @allure.description("Проверка получения заказов без авторизации возвращает ошибку 401")
    @allure.title("Получение заказов пользователя не авторизованного пользователя выдает ответ 401")
    def test_get_order_user_not_auth(self):
        with allure.step("Отправка GET запроса на получение заказов без авторизации"):
            r = requests.get(f"{Urls.MAIN_URL}{Handlers.GET_ORDERS}")
        
        with allure.step("Проверка получения ошибки 401"):
            assert r.status_code == 401 and r.json()['message'] == "You should be authorised"