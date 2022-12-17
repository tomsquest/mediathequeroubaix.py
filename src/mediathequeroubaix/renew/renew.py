from returns.io import IOResultE, impure_safe
from returns.pipeline import flow

from mediathequeroubaix.auth.authenticated_session import AuthenticatedSession
from mediathequeroubaix.get_loans.loan import Loans


def renew(session: AuthenticatedSession, loans: Loans) -> IOResultE[None]:
    return flow(
        (session, loans),
        _post_renew,
    )


@impure_safe
def _post_renew(data: tuple[AuthenticatedSession, Loans]) -> None:
    session, loans = data
    renewables = [loan for loan in loans.items if loan.renewable]
    if not renewables:
        print(f"No loan to renew for {session.username}")
    else:
        print(f"Will renew {len(renewables)} loans for {session.username}")
        response = session.session.post(
            "http://www.mediathequederoubaix.fr/espace_personnel",
            data={
                "submit_renew": "",
                "item_renew[]": [loan.itemnumber for loan in renewables],
            },
        )
        response.raise_for_status()
