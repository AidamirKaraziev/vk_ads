import requests
from fastapi import HTTPException

from settings import CLIENT_ID, CLIENT_SECRET


async def default_auth():
    url = "https://ads.vk.com/api/v2/oauth2/token.json"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.json()

    else:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )


def delete_oauth2_token(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
):
    """
    Удаляет OAuth2 токен с помощью POST-запроса к VK API.

    :param client_id: Идентификатор клиента (client_id)
    :param client_secret: Секрет клиента (client_secret)
    # :param user_identifier: Имя пользователя (username) или идентификатор пользователя (user_id)
    # :param identifier_type: Тип идентификатора, который передается (username или user_id)
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
    if response.status_code == 204 or response.status_code == 200:
        return response
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )


if __name__ == '__main__':
    pass
