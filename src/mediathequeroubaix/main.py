from dotenv import dotenv_values

from mediathequeroubaix.authenticate import authenticate
from mediathequeroubaix.print_loans import print_loans

if __name__ == "__main__":
    config = dotenv_values(".env")

    username = config.get("USERNAME")
    password = config.get("PASSWORD")
    if username and password:
        print(f"Getting loans of user: {username}")
        authenticated_session = authenticate(username, password)
        print_loans(authenticated_session)
    else:
        print("Missing USERNAME and PASSWORD in env")
