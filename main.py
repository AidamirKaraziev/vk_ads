from fastapi import FastAPI, HTTPException

from ads.ad_plans import get_ad_plans, create_ad_plan
from agents.clients import get_agency_clients
from auth.crud import (
    get_access_token_for_user,
    delete_oauth2_token_for_user,
    delete_all_tokens_for_user_2
)
from auth.new_token import get_vk_ads_token
from basic_functionality.crud import default_auth, delete_oauth2_token
from campaign import create_ad_campaign, get_ad_accounts
from manager.clients import get_manager_clients
from manager.manager import get_campaigns
from send import get_vk_url_info
from settings import (
    ACCESS_TOKEN,
    MANAGER_ACCESS_TOKEN,
    MANAGER_ID
)

app = FastAPI()


@app.get(
    path="/default-auth",
    summary="""
Получение дефолтного токена для агентства-организации. Чисто просмотр.
"""
)
async def default_auth_api():
    return await default_auth()


@app.get(
    path="/get-access-token",
    summary="Получение токена для Агентства-пользователя"
)
async def get_access_token_api():
    return get_access_token_for_user()


@app.delete(
    path="/token-for-user",
    summary="Удалить токен для пользователя"
)
async def delete_oauth2_token_for_user_api():
    return await delete_oauth2_token_for_user(
        identifier_type="user_id",
        user_identifier=MANAGER_ID
    )


@app.delete(
    path="/token-for-user-2",
    summary="Удалить токен для пользователя - 2"
)
async def delete_oauth2_token_for_user_api_2():
    return await delete_all_tokens_for_user_2(MANAGER_ID)


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
        access_token_manager = MANAGER_ACCESS_TOKEN
        access_token_agent = ACCESS_TOKEN
        print(1)
        ad_accounts = get_ad_accounts(access_token_agent)
        print(2)
        results = []
        accounts = ad_accounts.get("items")
        for account in accounts:
            account_id = account.get("user").get("id")
            result = create_ad_campaign(
                access_token=access_token_manager,
                client_id=account_id,
                campaign_data=campaign_data
            )
            results.append(result)

        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get(
    path="/get-agencies-client",
    summary="Получение всех рекламных кабинетов для клиентов"
)
async def get_agencies_client_api():
    return get_agency_clients()


@app.get("/get-vk-url-info")
async def get_vk_url_info_api():
    return get_vk_url_info()


@app.delete("/delete-oauth2-token")
async def delete_all_tokens():
    return delete_oauth2_token()


@app.get("/campaigns/")
def read_campaigns():
    """
    Получение списка рекламных кампаний для указанного клиента.
    """
    campaigns = get_campaigns()
    return campaigns


@app.get("/create-ad-plan/")
async def create_ad_plan_api():
    return create_ad_plan()


@app.get("/ad-plans")
async def get_ad_plans_api():
    return await get_ad_plans()


@app.get(
    path="/get-clients-for-manager",
    summary="Получение всех клиентов для менеджера"
)
async def get_manager_clients_api():
    return await get_manager_clients(ACCESS_TOKEN)


if __name__ == '__main__':
    pass
