"""
Authentication routines.


Environment variables
=====================

.. warning::
    For development only.  You don't need to set these during normal operation.

.. envvar:: NEXTSTRAIN_COGNITO_USER_POOL_ID

.. envvar:: NEXTSTRAIN_COGNITO_CLI_CLIENT_ID
"""
import os
from functools import partial
from sys import stderr
from typing import Dict, List, Optional

from . import config
from .errors import UserError
from .aws import cognito


# Section to use in config.SECRETS file
CONFIG_SECTION = "authn"

# Public ids.  Client id is specific to the CLI.
COGNITO_USER_POOL_ID = os.environ.get("NEXTSTRAIN_COGNITO_USER_POOL_ID") \
                    or "us-east-1_Cg5rcTged"

COGNITO_CLIENT_ID = os.environ.get("NEXTSTRAIN_COGNITO_CLI_CLIENT_ID") \
                 or "2vmc93kj4fiul8uv40uqge93m5"

CognitoSession = partial(cognito.Session, COGNITO_USER_POOL_ID, COGNITO_CLIENT_ID)


class User:
    """
    Data class holding information about a user.
    """
    username: str
    groups: List[str]
    email: str
    http_authorization: str

    def __init__(self, session: cognito.Session):
        assert session.id_claims

        self.username = session.id_claims["cognito:username"]
        self.groups   = session.id_claims["cognito:groups"]
        self.email    = session.id_claims["email"]

        self.http_authorization = f"Bearer {session.id_token}"


def login(username: str, password: str) -> User:
    """
    Authenticates the given *username* and *password*.

    Returns a :class:`User` object with information about the logged in user
    when successful.

    Raises a :class:`UserError` if authentication fails.
    """
    session = CognitoSession()

    try:
        session.authenticate(username, password)

    except cognito.NewPasswordRequiredError:
        raise UserError("Password change required.  Please login to Nextstrain.org first.")

    except cognito.NotAuthorizedError as error:
        raise UserError(f"Login failed: {error}")

    _save_tokens(session)
    print(f"Credentials saved to {config.SECRETS}.", file = stderr)

    return User(session)


def renew():
    """
    Renews existing tokens, if possible.

    Returns a :class:`User` object with renewed information about the logged in
    user when successful.

    Raises a :class:`UserError` if authentication fails.
    """
    session = CognitoSession()
    tokens = _load_tokens()
    refresh_token = tokens.get("refresh_token")

    if not refresh_token:
        return None

    try:
        session.renew_tokens(refresh_token = refresh_token)

    except (cognito.TokenError, cognito.NotAuthorizedError):
        return None

    _save_tokens(session)
    print(f"Renewed login credentials in {config.SECRETS}.", file = stderr)

    return User(session)


def logout():
    """
    Remove locally-saved credentials.

    The authentication tokens are not invalidated and will remain valid until
    they expire.  This does not contact Cognito and other devices/clients are
    not logged out of Nextstrain.org.
    """
    if config.remove(CONFIG_SECTION, config.SECRETS):
        print(f"Credentials removed from {config.SECRETS}.", file = stderr)
        print("Logged out.", file = stderr)
    else:
        print("Not logged in.", file = stderr)


def current_user() -> Optional[User]:
    """
    Information about the currently logged in user, if any.

    Returns a :class:`User` object after validating saved credentials, renewing
    and updating them if necessary.

    Returns ``None`` if there are no saved credentials or if they're unable to
    be automatically renewed.
    """
    session = CognitoSession()
    tokens = _load_tokens()

    try:
        try:
            session.verify_tokens(**tokens)

        except cognito.ExpiredTokenError:
            session.renew_tokens(refresh_token = tokens.get("refresh_token"))
            _save_tokens(session)
            print(f"Renewed login credentials in {config.SECRETS}.", file = stderr)

    except (cognito.TokenError, cognito.NotAuthorizedError):
        return None

    return User(session)


def _load_tokens() -> Dict[str, Optional[str]]:
    """
    Load id, access, and refresh tokens (if any) from the local secrets file.
    """
    def load(name):
        return config.get(CONFIG_SECTION, name, fallback = None, path = config.SECRETS)

    return {
        "id_token":      load("id_token"),
        "access_token":  load("access_token"),
        "refresh_token": load("refresh_token") }


def _save_tokens(session: cognito.Session):
    """
    Save id, access, and refresh tokens from the :class:`cognito.Session`
    *session* to the local secrets file.
    """
    def save(name, value):
        return config.set(CONFIG_SECTION, name, value, path = config.SECRETS)

    save("id_token",      session.id_token)
    save("access_token",  session.access_token)
    save("refresh_token", session.refresh_token)
