import requests
from fastapi import HTTPException

from settings import ACCESS_TOKEN


def get_agency_clients():
    url = "https://ads.vk.com/api/v2/agency/clients.json"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )

#
# def get_agencies_client():
#     url = "https://ads.vk.com/api/v2/agency/clients.json"
#
#     # Заголовки запроса
#     headers = {
#         "Authorization": f"Bearer {ACCESS_TOKEN}"
#     }
#
#     # Выполнение GET-запроса
#     response = requests.get(url, headers=headers)
#
#     # Проверка ответа
#     if response.status_code == 200:
#         # Если запрос успешен, выводим полученные данные
#         print("Ответ от сервера:", response.json())
#         return response.json()
#     else:
#         # Если произошла ошибка, выводим код ошибки и текст ответа
#         print("Ошибка:", response.status_code)
#         print("Ответ:", response.text)
#         return response.text
