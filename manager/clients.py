import requests
from fastapi import HTTPException


def get_manager_clients(access_token):
    url = "https://ads.vk.com/api/v3/manager/clients.json"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        clients_info = response.json()
        return clients_info
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )


if __name__ == '__main__':
    pass
