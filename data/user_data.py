from faker import Faker


class User:

    @staticmethod
    def create_data_user():
        fake = Faker()

        reg_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()}
        return reg_data

    data_correct = {
        "email": 'SergeyKulikov42123@ya.ru',
        "password": "SergeyKulikov42123"}

    data_negative = {
        "email": 'SergeyKulikov42@ya.ru',
        "password": "password"}

    data_double = {
        "email": 'SergeyKulikov42123@ya.ru',
        "password": "SergeyKulikov42123",
        "name": "Username"}

    data_without_email = {
        "email": '',
        "password": "SergeyKulikov42123",
        "name": "Сергей"}

    data_without_password = {
        "email": 'SergeyKulikov42123@ya.ru',
        "password": "",
        "name": "Сергей"}

    data_without_name = {
        "email": 'SergeyKulikov42123@ya.ru',
        "password": "SergeyKulikov42123",
        "name": ""}

    data_updated = {
        "email": 'SergeyKulikov42123@ya.ru',
        "password": "SergeyKulikov42123",
        "name": "Update"}