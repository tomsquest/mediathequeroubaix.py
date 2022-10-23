import requests
from dotenv import dotenv_values

from mediathequeroubaix.login import login
from mediathequeroubaix.print_loans import print_loans

if __name__ == "__main__":
    config = dotenv_values(".env")

    username = config.get("USERNAME")
    password = config.get("PASSWORD")
    if username and password:
        print(f"Getting loans of user: {username}")
        session = requests.Session()
        login(session=session, username=username, password=password)
        print_loans(session=session)
    else:
        print("Missing USERNAME and PASSWORD in env")
