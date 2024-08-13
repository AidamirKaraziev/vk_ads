import requests

from settings import CLIENT_ID, CLIENT_SECRET


# CLIENT_ID = 'your_client_id_here'
# CLIENT_SECRET = 'your_client_secret_here'
REDIRECT_URI = 'localhost:9009'
# AUTHORIZATION_CODE = 'your_authorization_code_here'


# Пример использования
if __name__ == "__main__":
    pass

#
# def get_access_token_manager():
#     # URL для получения токена
#     url = "https://oauth.vk.com/access_token"
#
#     # Параметры запроса
#     params = {
#         "client_id": CLIENT_ID,
#         "client_secret": CLIENT_SECRET,
#         "redirect_uri": REDIRECT_URI,
#         "code": AUTHORIZATION_CODE
#     }
#
#     # Выполняем POST-запрос для получения токена
#     response = requests.get(url, params=params)
#
#     # Проверяем статус ответа
#     if response.status_code == 200:
#         token_data = response.json()
#         print("Access Token:", token_data["access_token"])
#         return token_data["access_token"]
#     else:
#         print("Ошибка:", response.status_code)
#         print("Ответ:", response.text)
#         return None