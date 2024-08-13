import requests
from fastapi import HTTPException

from settings import CLIENT_ID, ACCESS_TOKEN


async def get_ad_plans():
    url = "https://ads.vk.com/api/v2/ad_plans.json"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    # Добавляем параметр client_id, если он указан
    params = {}
    params["client_id"] = CLIENT_ID

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )


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
        return response.json()
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )


if __name__ == "__main__":
    pass
