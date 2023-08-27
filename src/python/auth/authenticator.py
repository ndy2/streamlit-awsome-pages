from dataclasses import asdict
from datetime import datetime, timezone, timedelta
from typing import Optional

from python.auth import sessions, cookies
from python.auth.domain import User, UserSource
from python.auth.support import JwtService

Authentication = tuple[bool, Optional[User]]
NOT_AUTHENTICATED = False, None
timezone_kst = timezone(timedelta(hours=9))


class Authenticator:

    def __init__(self,
                 user_source: UserSource,
                 jwt_service: JwtService
                 ) -> None:
        super().__init__()
        self._user_source = user_source
        self._jwt_service = jwt_service
        self._set_default_sessions()

    def check_form_authentication(self, login_form_with_input) -> tuple[Authentication, bool]:
        self._set_default_sessions()
        # check form authentication
        submit, username, password = login_form_with_input()
        if not submit:
            return NOT_AUTHENTICATED, False

        form_authenticated, form_user = self._check_username_password_authentication(username, password)
        if form_authenticated:
            self._add_cookie(form_user)
            self._set_session_authentication_success(form_user)
        return (form_authenticated, form_user), True

    def check_cookie_authentication(self) -> Authentication:
        self._set_default_sessions()
        # check session authentication
        if sessions.get("authenticated") and not self._expired(sessions.get("exp")):
            return True, sessions.get("user")
        if sessions.get("logout") is None:
            return NOT_AUTHENTICATED

        # check cookie authentication
        cookie_token = cookies.get_all("token").get("token")
        if cookie_token is None:
            return NOT_AUTHENTICATED

        # parse jwt payload
        payload = self._jwt_service.decode(cookie_token)
        if not self._expired(payload.get("exp")):
            cookie_user = User(
                username=payload.get("username"),
                password=payload.get("password"),
                age=payload.get("age")
            )
            self._set_session_authentication_success(cookie_user)
            return True, cookie_user
        return NOT_AUTHENTICATED

    def _check_username_password_authentication(self, username, password) -> Authentication:
        found_user = self._user_source.load_by_username(username)
        if found_user is None or found_user.password != password:
            return NOT_AUTHENTICATED
        return True, found_user

    def _add_cookie(self, user: User):
        exp = self._exp_timestamp()
        cookies.set(
            cookie="token",
            val=self._jwt_service.encode(asdict(user) | {"exp": exp.timestamp()}),
            expires_at=exp
        )

    @staticmethod
    def _set_session_authentication_success(user: User):
        sessions.set("authenticated", True)
        sessions.set("user", user)
        sessions.set("exp", Authenticator._exp_timestamp().timestamp())

    @staticmethod
    def _set_default_sessions():
        sessions.set_if_none("authenticated", False)
        sessions.set_if_none("user", None)
        sessions.set_if_none("logout", False)
        sessions.set_if_none("exp", False)

    @staticmethod
    def logout():
        cookies.delete("token")
        sessions.set("logout", True)
        sessions.set("authenticated", None)
        sessions.set("user", None)

    @staticmethod
    def _expired(exp_timestamp: float):
        return exp_timestamp < datetime.now().timestamp()

    @staticmethod
    def _exp_timestamp() -> datetime:
        return datetime.now() + timedelta(hours=1)
