import requests
from settings import ACCESS_TOKEN


def get_vk_url_info():
    # URL запроса
    url = "https://ads.vk.com/api/v1/urls/"

    # Параметры запроса
    params = {
        "url": "https://vk.com/vk"
    }

    # Заголовки запроса
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    # Выполнение GET-запроса
    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    # Проверка ответа
    if response.status_code == 200:
        print("Ответ от сервера:", response.json())
        return response.json()
    else:
        print("Ошибка:", response.status_code)
        print("Ответ:", response.text)
        return f"Ответ: {response.text}"


if __name__ == "__main__":
    pass
