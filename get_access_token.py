import requests

from settings import CLIENT_ID, CLIENT_SECRET, AGENCY_CLIENT_NAME


def get_access_token():
    # URL для получения токена
    url = "https://ads.vk.com/api/v2/oauth2/token.json"

    # Параметры запроса
    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        # "agency_client_name": AGENCY_CLIENT_NAME,
        # "scope": "ads"
    }

    # Выполняем POST-запрос
    response = requests.post(url, data=payload)

    # Проверяем статус ответа
    if response.status_code == 200:
        token_data = response.json()
        print("token_data", token_data)
        print("Access Token:", token_data["access_token"])
        return token_data
    else:
        print("Ошибка:", response.status_code)
        print("Ответ:", response.text)
        print(response)
        return response.text


def delete_oauth2_token(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        # user_identifier="Russian Robotics Ads",
        # identifier_type="username",
):
    """
    Удаляет OAuth2 токен с помощью POST-запроса к VK API.

    :param client_id: Идентификатор клиента (client_id)
    :param client_secret: Секрет клиента (client_secret)
    :param user_identifier: Имя пользователя (username) или идентификатор пользователя (user_id)
    :param identifier_type: Тип идентификатора, который передается (username или user_id)
    :return: Ответ от сервера в формате JSON или текст ошибки
    """

    url = "https://ads.vk.com/api/v2/oauth2/token/delete.json"

    # Подготовка данных для запроса
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        # identifier_type: user_identifier
    }

    # Заголовки запроса
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Выполнение POST-запроса
    response = requests.post(url, headers=headers, data=data)

    # Проверка ответа
    if response.status_code == 200:
        return response.json()  # Возвращаем данные в формате JSON
    else:
        print(f"Ошибка: {response.status_code}\nОтвет: {response.text}")
        return f"Ошибка: {response.status_code}\nОтвет: {response.text}"


if __name__ == '__main__':
    pass
    # get_access_token()
