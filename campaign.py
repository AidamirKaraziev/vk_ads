import requests
from fastapi import FastAPI, HTTPException

from settings import AGENCY_CLIENT_ID, CLIENT_SECRET, CLIENT_ID

app = FastAPI()


def get_ad_accounts(access_token):
    url = "https://ads.vk.com/api/v2/agency/clients.json"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(response.json())
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )


def create_ad_campaign(
        *,
        access_token: str,
        client_id: int,
        campaign_data: dict,
):
    print("777 client_id", client_id)
    url = f"https://ads.vk.com/api/v2/ad_plans.json"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "client_id": client_id,
        "name": campaign_data["name"],
        "status": "active",  # Возможно, придется поменять на "paused" или другой статус
        "date_start": campaign_data["date_start"],  # Формат даты: "YYYY-MM-DD HH:MM:SS"
        "date_end": campaign_data["date_end"],  # Формат даты: "YYYY-MM-DD HH:MM:SS"
        "autobidding_mode": "max_goals",  # Автоматическое управление ставками
        "budget_limit_day": campaign_data["budget_limit_day"],  # Дневной лимит бюджета
        "budget_limit": campaign_data["budget_limit"],  # Общий лимит бюджета
        "objective": "playersengagement",  # Цель кампании
        "ad_groups": []  # В этой версии пока оставляем пустым
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(response.json())
        error_data = {
            "code": response.json()['error']["code"],
            "message": response.json()['error']["message"],
            "required_permission": response.json()['error']["required_permission"],
        }
        # raise HTTPException(
        #     status_code=response.status_code,
        #     detail=error_data
        # )


if __name__ == "__main__":
    pass
