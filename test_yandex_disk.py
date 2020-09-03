
import unittest
import requests
from yandex_disk import YD_URL, YANDEX_UPLOAD_URL, TOKEN_YD, YD_OAUTH, id_VK, yandex_oauth_header, YDUser

class TestYandexDisk(unittest.TestCase):
    def setUp(self):
        self.user_test = TestYandexDisk()

  #Each test method starts with the keyword test_
    def test_yandex_folder(self):
        yandex_folder_url = f'{YD_URL}{"/resources"}'
        # доп параметры для создания папки ЯД БЕЗ overwrite!
        yandex_folder_params = {
            'path': f'{"id_VK-"}{id_VK}'
        }
        response = user1.put_request(yandex_folder_url, params=yandex_folder_params, headers=yandex_oauth_header)
        return response
        self.assertEqual(self.user_test.test_yandex_folder(response), 200)

    def test_yandex_folder_not(self):
        yandex_folder_url = f'{YD_URL}{"/resources"}'
        # доп параметры для создания папки ЯД БЕЗ overwrite!
        yandex_folder_params = {
            'path': f'{"id_VK-"}{id_VK}'
        }
        response = user1.put_request(yandex_folder_url, params=yandex_folder_params, headers=yandex_oauth_header)
        return response
        #self.assertEqual(self.user_test.test_yandex_folder_not(response), 4*)
        self.assertTrue(400 <= response < 500)

user1 = YDUser()
user1.yandex_folder()

user_test = TestYandexDisk()
###user_test.test_yandex_folder()

# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()

