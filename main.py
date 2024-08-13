from fastapi import FastAPI, HTTPException

from agents_1 import get_agencies_client, create_ad_plan
from auth.new_token import get_vk_ads_token
from campaign import create_ad_campaign, get_ad_accounts
from auth.get_access_token import (
    delete_oauth2_token,
    get_access_token,
    default_auth
)
from manager.clients import get_manager_clients
from manager.manager import get_campaigns
from send import get_vk_url_info
from settings import ACCESS_TOKEN

app = FastAPI()


@app.get(
    path="/default-auth",
    summary="Получение дефолтного токена для агентства"
)
async def default_auth_api():
    return await default_auth()


@app.get("/get-access-token")
async def get_access_token_api():
    return get_access_token()


@app.get(
    path="/get-good-access-token",
    summary="""
Получение токена Агентства со необходимыми правами к созданию рекламной компании
""" # noqa E501
)
async def get_campaigns_api():
    token_info = await get_vk_ads_token(
        client_username="vkads_850957759@vk@2560596",
        # client_username="7084eeefce@agency_client",
        agency_access_token=ACCESS_TOKEN
    )
    print(token_info)
    return token_info


@app.post("/create-campaigns/")
def create_campaigns_for_all_clients(
        campaign_data=None
):
    if campaign_data is None:
        campaign_data = {
            "name": "Test Campaign",
            "date_start": "2024-08-10",
            "date_end": "2024-08-20",
            "budget_limit_day": 1000,
            "budget_limit": 10000
        }
    try:
        access_token = ACCESS_TOKEN
        print(1)
        ad_accounts = get_ad_accounts(access_token)
        print(2)
        results = []
        accounts = ad_accounts.get("items")
        for account in accounts:
            account_id = account.get("user").get("id")
            result = create_ad_campaign(
                access_token=access_token,
                client_id=account_id,
                campaign_data=campaign_data
            )
            results.append(result)

            return account
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get(
    path="/get-clients-for-manager",
    summary="Получение всех клиентов для менеджера"
)
async def get_manager_clients_api():
    return await get_manager_clients(ACCESS_TOKEN)


@app.get(
    path="/get-agencies-client",
    summary="Получение всех рекламных кабинетов для клиентов"
)
async def get_agencies_client_api():
    return get_agencies_client()


@app.get("/get-vk-url-info")
async def get_vk_url_info_api():
    return get_vk_url_info()


@app.delete("/delete-oauth2-token")
async def delete_all_tokens():
    return delete_oauth2_token()


@app.get("/get-ad-accounts")
async def get_ad_accounts_api():
    return get_ad_accounts(ACCESS_TOKEN)


@app.get("/campaigns/")
def read_campaigns():
    """
    Получение списка рекламных кампаний для указанного клиента.
    """
    try:
        campaigns = get_campaigns()
        return campaigns
    except HTTPException as e:
        raise e


@app.get("/create-ad-plan/")
async def create_ad_plan_api():
    return create_ad_plan()


if __name__ == '__main__':
    pass
