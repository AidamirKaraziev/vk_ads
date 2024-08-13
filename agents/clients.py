# import requests
# from fastapi import HTTPException
#
#
# def get_agency_client_info(access_token, client_id):
#     url = f"https://ads.vk.com/api/v2/agency/clients/{client_id}.json"
#     headers = {
#         "Authorization": f"Bearer {access_token}"
#     }
#
#     response = requests.get(url, headers=headers)
#
#     if response.status_code == 200:
#         client_info = response.json()
#         return client_info
#     else:
#         print(f"Error: {response.status_code}, {response.text}")
#         raise HTTPException(
#             status_code=response.status_code,
#             detail=response.text
#         )
#
# # Пример использования:
# # access_token = "YOUR_ACCESS_TOKEN"
# # client_id = "CLIENT_ID"
#
# client_info = get_agency_client_info(access_token, client_id)
# #
# # if client_info:
# #     print("Client Info:", client_info)
# #