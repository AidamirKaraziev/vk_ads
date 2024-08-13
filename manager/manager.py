from fastapi import HTTPException
import requests

from settings import CLIENT_ID, ACCESS_TOKEN, MANAGER_ACCESS_TOKEN


def get_campaigns():
    url = "https://ads.vk.com/api/v2/ad_plans.json"
    headers = {
        "Authorization": f"Bearer {MANAGER_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    params = {
        "client_id": CLIENT_ID
    }
    response = requests.get(url, headers=headers, params=params)
    print(response)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )


# Запуск сервера
if __name__ == "__main__":
    pass
