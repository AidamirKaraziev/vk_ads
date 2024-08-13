import requests
from fastapi import FastAPI, HTTPException

from settings import AGENCY_CLIENT_ID, CLIENT_SECRET, CLIENT_ID

app = FastAPI()


def get_access_token_new():
    url = "https://ads.vk.com/api/v2/oauth2/token.json"
    payload = {
        "grant_type": "agency_client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "agency_client_id": AGENCY_CLIENT_ID,
        "scope": "ads,view_campaigns,"
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )


def get_ad_accounts(access_token):
    url = "https://ads.vk.com/api/v2/agency/clients.json"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # print(response.json())
        return response.json()
    else:
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
        "status": "active",
        # Возможно, придется поменять на "paused" или другой статус
        "date_start": campaign_data["date_start"],
        # Формат даты: "YYYY-MM-DD HH:MM:SS"
        "date_end": campaign_data["date_end"],
        # Формат даты: "YYYY-MM-DD HH:MM:SS"
        "autobidding_mode": "max_goals",  # Автоматическое управление ставками
        "budget_limit_day": campaign_data["budget_limit_day"],
        # Дневной лимит бюджета
        "budget_limit": campaign_data["budget_limit"],  # Общий лимит бюджета
        "objective": "playersengagement",  # Цель кампании
        "ad_groups": []  # В этой версии пока оставляем пустым
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        # print(response)

        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )


if __name__ == "__main__":
    pass
