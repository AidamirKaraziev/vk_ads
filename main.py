from fastapi import FastAPI, HTTPException

from agents import get_agencies_client
from campaign import create_ad_campaign, get_ad_accounts
from auth.get_access_token import delete_oauth2_token, get_access_token
from manager.manager import get_campaigns
from send import get_vk_url_info
from settings import ACCESS_TOKEN

app = FastAPI()


@app.get("/get-access-token")
async def get_access_token_api():
    return get_access_token()


@app.post("/create-campaigns/")
def create_campaigns_for_all_clients(
        campaign_data: dict = {
            "name": "Test Campaign",
            "date_start": "2024-08-10",
            "date_end": "2024-08-20",
            "budget_limit_day": 1000,
            "budget_limit": 10000
        }
):
    try:
        access_token = ACCESS_TOKEN
        print(1)
        ad_accounts = get_ad_accounts(access_token)
        print(2)
        results = []
        accounts = ad_accounts.get("items")
        for account in accounts:
            account_id = account.get("user").get("id")
            print(account_id)
            result = create_ad_campaign(
                access_token=access_token,
                client_id=account_id,
                campaign_data=campaign_data
            )
            results.append(result)

            return account
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/get-agencies-client")
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
