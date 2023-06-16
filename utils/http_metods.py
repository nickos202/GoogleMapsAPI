import requests
import allure
from utils.logger import Logger

"""Список http методов"""


class Http_metods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        with allure.step("Step - GET"):
            Logger.add_requst(url, method="GET")
            result = requests.get(url, headers=Http_metods.headers, cookies=Http_metods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("Step - POST"):
            Logger.add_requst(url, method="POST")
            result = requests.post(url, json=body, headers=Http_metods.headers, cookies=Http_metods.cookie)
            Logger.add_response(result)
            return result


    @staticmethod
    def put(url, body):
        with allure.step("Step - PUT"):
            Logger.add_requst(url, method="PUT")
            result = requests.put(url, json=body, headers=Http_metods.headers, cookies=Http_metods.cookie)
            Logger.add_response(result)
            return result


    @staticmethod
    def delete(url, body):
        with allure.step("Step 1 - DELETE"):
            Logger.add_requst(url, method="DELETE")
            result = requests.delete(url, json=body, headers=Http_metods.headers, cookies=Http_metods.cookie)
            Logger.add_response(result)
            return result