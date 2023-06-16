# from requests import Response
import json

import allure
from utils.api import Google_maps_api
from utils.cheking import Cheking

"""Создание, изменение, удаление новой локации"""

@allure.epic("Test create place")
class Test_create_place:

    @allure.description("Создание, изменение и удаление новой локации.")
    def test_create_nae_place(self):
        print("Метод Post")
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Cheking.check_status_code(result_post, 200)
        Cheking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Cheking.check_json_value(result_post, 'status', 'OK')
        # token = json.loads(result_post.text)
        # print(list(token))

        print("Метод GET_POST")
        result_get = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                              'website', 'language'])
        Cheking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print("Метод PUT")
        result_put = Google_maps_api.put_new_place(place_id)
        Cheking.check_status_code(result_put, 200)
        Cheking.check_json_token(result_put, ['msg'])
        Cheking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("Метод GET_PUT")
        result_get = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                              'website', 'language'])
        Cheking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print("Метод DELETE")
        result_delete = Google_maps_api.delete_new_place(place_id)
        Cheking.check_status_code(result_delete, 200)
        Cheking.check_json_token(result_delete, ['status'])
        Cheking.check_json_value(result_delete, 'status', 'OK')

        print("Метод GET_DELETE")
        result_get = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 404)
        Cheking.check_json_token(result_put, ['msg'])
        Cheking.check_json_search_word_in_value(result_get, 'msg', 'failed')


        print("Тестирование создания, изменения, удаления новой локации прошло успешно.")