from dotenv import dotenv_values
from returns.io import IOFailure, IOSuccess
from returns.result import Success

from mediathequeroubaix.authenticate import authenticate
from mediathequeroubaix.print_loans import print_loans

if __name__ == "__main__":
    config = dotenv_values(".env")

    username = config.get("USERNAME")
    password = config.get("PASSWORD")
    if username and password:
        print(f"Getting loans of user: {username}")
        match authenticate(username, password):
            case IOSuccess(Success(authenticated_session)):
                print_loans(authenticated_session)
            case IOFailure(failure):
                print("❌ FAILURE!", failure)
    else:
        print("Missing USERNAME and PASSWORD in env")
