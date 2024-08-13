import requests
from fastapi import HTTPException

from settings import CLIENT_ID, CLIENT_SECRET


async def get_vk_ads_token(
        *,
        client_username: str,
        agency_access_token: str
):
    url = "https://ads.vk.com/api/v2/oauth2/token.json"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "agency_client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "agency_client_name": client_username,
        "access_token": agency_access_token,
        "scope": ["ads", "read_ads", "create_ads", "read_payments"]
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        token_info = response.json()
        return token_info
    else:
        print(f"Error: {response.status_code}, {response.text}")
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )


if __name__ == '__main__':
    pass
