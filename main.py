from fastapi import FastAPI, HTTPException

from campaign import create_ad_campaign, get_ad_accounts
from get_access_token import delete_oauth2_token, get_access_token
from send import get_vk_url_info

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/get-vk-url-info")
async def get_vk_url_info_api():
    return get_vk_url_info()


@app.delete("/delete-oauth2-token")
async def delete_all_tokens():
    return delete_oauth2_token()


@app.get("/get-access-token")
async def get_access_token_api():
    return get_access_token()


@app.get("/get-ad-accounts")
async def get_ad_accounts_api():
    return get_ad_accounts("hejl7F4b2v9btiD2sytN0JomQxCTUlkFl0eL10MOtx0JPoKVDuoyxqY1QcTt39KCP7C8EiYCNTP5KJ9NpQZfEExdBBQ4f0kf3Z42tSYDmipWBn6ehVEP1jqd64YCAR4vNmDSwDrMce3Ck1rClLd3FbMhWoQcVBgHtCOZlS8Tirr4GYE6IVjalMJjHMDj5Ed7gwmpJ9XIW4TRFUWx")


@app.post("/create-campaigns/")
def create_campaigns_for_all_clients(campaign_data: dict):
    try:
        # access_token = get_access_token()
        access_token = "hejl7F4b2v9btiD2sytN0JomQxCTUlkFl0eL10MOtx0JPoKVDuoyxqY1QcTt39KCP7C8EiYCNTP5KJ9NpQZfEExdBBQ4f0kf3Z42tSYDmipWBn6ehVEP1jqd64YCAR4vNmDSwDrMce3Ck1rClLd3FbMhWoQcVBgHtCOZlS8Tirr4GYE6IVjalMJjHMDj5Ed7gwmpJ9XIW4TRFUWx"
        ad_accounts = get_ad_accounts(access_token)

        results = []
        # print("12312", ad_accounts)
        accounts = ad_accounts.get("items")
        # print(ad_accounts.get("items"))
        for account in accounts:
            print("account", account)
            print("account_id", account.get("user").get("id"))
            account_id = account.get("user").get("id")
            result = create_ad_campaign(
                access_token=access_token,
                client_id=account_id,
                campaign_data=campaign_data
            )
            results.append(result)

            return account

        # return {"success": True, "campaigns": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

