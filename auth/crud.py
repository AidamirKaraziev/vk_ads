import requests
from fastapi import HTTPException

from settings import (
    CLIENT_ID,
    CLIENT_SECRET,
    AGENCY_CLIENT_ID,
    AGENCY_CLIENT_NAME,
    MY_AGENCY, ACCESS_TOKEN,
)


# def get_access_token_for_user():
#     # URL для получения токена
#     url = "https://ads.vk.com/api/v2/oauth2/token.json"
#
#     # дефолтный токен агентства
#     payload = {
#         "grant_type": "agency_client_credentials",
#         "client_id": CLIENT_ID,
#         "client_secret": CLIENT_SECRET,
#         "scope": "offline"
#     }
#
#     # Выполняем POST-запрос
#     response = requests.post(url, data=payload)
#
#     # Проверяем статус ответа
#     if response.status_code == 200:
#         token_data = response.json()
#         return token_data
#     else:
#         raise HTTPException(status_code=response.status_code, detail=response.text)


def get_access_token_for_user(
        # agency_client_id=None,
        # agency_client_name=None
):
    # URL для получения токена
    url = "https://ads.vk.com/api/v2/oauth2/token.json"

    # Основной payload с необходимыми параметрами
    payload = {
        "grant_type": "agency_client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        # "scope": "ads,read_ads,create_ads,edit_ads"  # Указываем необходимые scope
    }
    agency_client_id = AGENCY_CLIENT_ID
    agency_client_name = MY_AGENCY
    # Добавляем идентификатор или имя клиента агентства
    if agency_client_id:
        payload["agency_client_id"] = agency_client_id
    elif agency_client_name:
        payload["agency_client_name"] = agency_client_name
    else:
        raise ValueError("Either agency_client_id or agency_client_name must be provided.")

    # Выполняем POST-запрос
    response = requests.post(url, data=payload)

    # Проверяем статус ответа
    if response.status_code == 200:
        token_data = response.json()
        return token_data
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)


async def delete_oauth2_token_for_user(
        *,
        user_identifier: int = 21892461,
        identifier_type: str = "user_id"
):
    """
    Удаляет OAuth2 токен с помощью POST-запроса к VK API.

    :param user_identifier: Имя пользователя (username) или идентификатор пользователя (user_id)
    :param identifier_type: Тип идентификатора, который передается (username или user_id)
    :return: Ответ от сервера в формате JSON или текст ошибки
    """

    url = "https://ads.vk.com/api/v2/oauth2/token/delete.json"

    # Подготовка данных для запроса
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "identifier_type": identifier_type,
        "user_identifier": user_identifier
    }

    # Заголовки запроса
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Выполнение POST-запроса
    response = requests.post(url, headers=headers, data=data)
    print(response)
    # Проверка ответа
    if response.status_code == 204 or response.status_code == 200:
        return response
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )


def delete_all_tokens_for_user_2(
        user_id: int = 21892461
):
    # URL для получения всех токенов (например, если API предоставляет такой метод)
    list_tokens_url = "https://ads.vk.com/api/v2/agency/tokens.json"

    # URL для удаления токена
    delete_token_url = "https://ads.vk.com/api/v2/oauth2/token/delete.json"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Получаем список токенов (если API поддерживает такой запрос)
    try:
        response = requests.get(list_tokens_url, headers=headers, params={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET
        })
        response.raise_for_status()
        tokens = response.json().get('tokens',
                                     [])  # Предполагается, что список токенов возвращается в поле 'tokens'
    except requests.RequestException as e:
        raise HTTPException(status_code=e.response.status_code,
                            detail=e.response.text)

    # Удаляем каждый токен
    for token in tokens:
        try:
            delete_response = requests.post(
                delete_token_url,
                headers=headers,
                data={
                    "client_id": CLIENT_ID,
                    "client_secret": CLIENT_SECRET,
                    "user_identifier": user_id,
                    "identifier_type": "user_id",
                    # Тип идентификатора
                    "token": token
                    # Убедитесь, что API требует токен для удаления
                })
            delete_response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to delete token {token}: {e.response.text}")

    return {"status": "All tokens deleted"}


def delete_all_tokens_for_user_2(
        user_id: int = 21892461
):
    # URL для получения всех токенов
    list_tokens_url = "https://ads.vk.com/api/v2/agency/tokens.json"

    # URL для удаления токена
    delete_token_url = "https://ads.vk.com/api/v2/oauth2/token/delete.json"

    # Заголовки запроса для получения токенов
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        # Добавляем токен или авторизацию, если требуется
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Получаем список токенов (если API поддерживает такой запрос)
    try:
        response = requests.get(list_tokens_url, headers=headers, params={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET
        })
        response.raise_for_status()
        tokens = response.json().get('tokens',
                                     [])  # Предполагается, что список токенов возвращается в поле 'tokens'
    except requests.RequestException as e:
        raise HTTPException(status_code=e.response.status_code,
                            detail=e.response.text)

    # Удаляем каждый токен
    for token in tokens:
        try:
            delete_response = requests.post(
                delete_token_url,
                headers=headers,
                data={
                    "client_id": CLIENT_ID,
                    "client_secret": CLIENT_SECRET,
                    "user_identifier": user_id,
                    "identifier_type": "user_id",
                    "token": token
                }
            )
            delete_response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to delete token {token}: {e.response.text}")

    return {"status": "All tokens deleted"}


if __name__ == '__main__':
    pass
