import requests
from settings import ACCESS_TOKEN


def get_agencies_client():
    url = "https://ads.vk.com/api/v2/agency/clients.json"

    # Заголовки запроса
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    # Выполнение GET-запроса
    response = requests.get(url, headers=headers)

    # Проверка ответа
    if response.status_code == 200:
        # Если запрос успешен, выводим полученные данные
        print("Ответ от сервера:", response.json())
        return response.json()
    else:
        # Если произошла ошибка, выводим код ошибки и текст ответа
        print("Ошибка:", response.status_code)
        print("Ответ:", response.text)
        return response.text


def ad_plans():
    url = "https://ads.vk.com/api/v2/ad_plans.json"

    # Заголовки запроса
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    # Выполнение GET-запроса
    response = requests.get(url, headers=headers)

    # Проверка ответа
    if response.status_code == 200:
        # Если запрос успешен, выводим полученные данные
        print("Ответ от сервера:", response.json())
        return response.json()
    else:
        # Если произошла ошибка, выводим код ошибки и текст ответа
        print("Ошибка:", response.status_code)
        print("Ответ:", response.text)
        return response.text


def create_ad_plan():
    # URL для POST-запроса
    url = "https://ads.vk.com/api/v2/ad_plans.json"

    # Заголовки запроса
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    # Данные для создания новой кампании
    payload = {
        "name": "Моя новая кампания",
        "status": "active",
        "date_start": "2022-04-01 00:00:00",
        "date_end": "2022-04-15 00:00:00",
        "autobidding_mode": "max_goals",
        "budget_limit_day": "1000",
        "budget_limit": "5000",
        "enable_utm": "False",
        "enable_offline_goals": "False",
        "objective": "playersengagement",
        "ad_groups": []
    }

    # Выполнение POST-запроса
    response = requests.post(url, headers=headers, json=payload)

    # Проверка ответа
    if response.status_code == 200:
        # Если запрос успешен, выводим полученные данные
        print("Кампания успешно создана:", response.json())
        return response.json()
    else:
        # Если произошла ошибка, выводим код ошибки и текст ответа
        print("Ошибка:", response.status_code)
        print("Ответ:", response.text)
        return response.text


if __name__ == "__main__":
    pass
