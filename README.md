# Diplom_2 API-тестирование
В данном проекте тестировались эндпоинты API для Stellar Burgers.
URL стенда: https://stellarburgers.education-services.ru/

Проект состоит из файлов:
data/ - папка с данными для тестов
- ingredients_data - файл с идентификаторами ингредиентов
- urls - файл с URL стенда и ручками
- user_data - файл с данными пользователя
tests/ - папка с тестами
- test_create_user - файл с тестами по созданию пользователя в системе
- test_login_user - файл с тестами авторизации 
- test_create_order - файл с тестами создания заказа
- test_get_order_for_user - файл с тестами получения заказа пользователя
- test_change_user_data - файл с тестами изменения данных пользователя
conftest - файл с фикстурами
requirements.txt - файл с зависимостями

Для запуска тестов из директории tests необходимо выполнить команду: pytest tests --alluredir=allure_results

Посмотреть отчет выполненных тестов: allure serve allure_results
