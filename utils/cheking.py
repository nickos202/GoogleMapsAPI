"""Методы для проверки запросов"""
import json

from requests import Response


class Cheking:

    """"Метод для проверки статус-кода"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Статус код верный: " + str(response.status_code))
        else:
            print("Статус код неверный: " + str(response.status_code))


    """Метод для проверки наличия обязательных полей"""
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")



    """Метод для проверки значений обязательных полей"""
    @staticmethod
    def check_json_value(response: Response, fild_name, expected_value):
        check = response.json()
        check_info = check.get(fild_name)
        assert check_info == expected_value
        print(fild_name + " верен")



    """Метод для проверки значений обязательных полей в ответе запроса по заданному слову"""
    @staticmethod
    def check_json_search_word_in_value(response: Response, fild_name, search_word):
        check = response.json()
        check_info = check.get(fild_name)
        if search_word in check_info:
            print("Слово " + search_word + " присутствует.")
        else:
            print("Слово " + search_word + " присутствует.")
