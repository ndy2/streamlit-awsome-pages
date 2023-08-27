from dataclasses import asdict
from datetime import datetime, timezone, timedelta
from typing import Optional

from extra_streamlit_components import CookieManager

from python.auth.domain import User, UserSource
from python.auth.support import JwtService, SessionManager

Authentication = tuple[bool, Optional[User]]
NOT_AUTHENTICATED = False, None
timezone_kst = timezone(timedelta(hours=9))


class Authenticator:

    def __init__(self,
                 user_source: UserSource,
                 jwt_service: JwtService,
                 cookies: CookieManager,
                 sessions: SessionManager
                 ) -> None:
        super().__init__()
        self.user_source = user_source
        self.jwt_service = jwt_service
        self.cookies = cookies
        self.sessions = sessions
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
        if self.sessions.get("authenticated") and not self._expired(self.sessions.get("exp")):
            return True, self.sessions.get("user")
        if self.sessions.get("logout") is None:
            return NOT_AUTHENTICATED

        # check cookie authentication
        cookie_token = self.cookies.get_all("token").get("token")
        if cookie_token is None:
            return NOT_AUTHENTICATED

        # parse jwt payload
        payload = self.jwt_service.decode(cookie_token)
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
        found_user = self.user_source.load_by_username(username)
        if found_user is None or found_user.password != password:
            return NOT_AUTHENTICATED
        return True, found_user

    def _add_cookie(self, user: User):
        exp = self._exp_timestamp()
        self.cookies.set(
            cookie="token",
            val=self.jwt_service.encode(asdict(user) | {"exp": exp.timestamp()}),
            expires_at=exp
        )

    def _set_session_authentication_success(self, user: User):
        self.sessions.set("authenticated", True)
        self.sessions.set("user", user)
        self.sessions.set("exp", self._exp_timestamp().timestamp())

    def _set_default_sessions(self):
        self.sessions.set_if_none("authenticated", False)
        self.sessions.set_if_none("user", None)
        self.sessions.set_if_none("logout", False)
        self.sessions.set_if_none("exp", False)

    @staticmethod
    def _expired(exp_timestamp: float):
        return exp_timestamp < datetime.now().timestamp()

    @staticmethod
    def _exp_timestamp() -> datetime:
        return datetime.now() + timedelta(hours=1)
