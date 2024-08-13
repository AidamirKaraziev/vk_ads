import os
from dotenv import load_dotenv

# Загрузка переменных из .env файла
load_dotenv()

# Получение переменных
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
AGENCY_CLIENT_NAME = os.getenv("AGENCY_CLIENT_NAME")
AGENCY_CLIENT_ID = os.getenv("AGENCY_CLIENT_ID")
MY_AGENCY = os.getenv("MY_AGENCY")
MANAGER_ACCESS_TOKEN = os.getenv("MANAGER_ACCESS_TOKEN")

if __name__ == '__main__':
    pass
