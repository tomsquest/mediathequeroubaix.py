from requests import Session


def login(*, session: Session, username: str, password: str) -> None:
    response = session.post(
        "http://www.mediathequederoubaix.fr",
        data={
            "name": username,
            "pass": password,
            "form_id": "user_login_block",
        },
    )
    response.raise_for_status()

    is_connected = response.text.find("Me déconnecter") != -1
    print("Connected?", is_connected)
