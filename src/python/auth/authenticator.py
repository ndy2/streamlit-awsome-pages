from typing import Optional

import extra_streamlit_components as stx

from python.auth.domain import User, UserSource

Authentication = tuple[bool, Optional[User]]
NOT_AUTHENTICATED = False, None


class Authenticator:

    def __init__(self, user_source: UserSource) -> None:
        super().__init__()
        self.user_source = user_source
        self.cookie_manager = stx.CookieManager()

    def check_cookie_and_form_authentication(self, login_form_with_input) -> Authentication:
        cookie_authenticated, cookie_authenticated_user = self.check_cookie_authentication()

        form_authenticated, form_authenticated_user = NOT_AUTHENTICATED
        if cookie_authenticated is False:
            form_authenticated, form_authenticated_user = self._check_form_authentication(*login_form_with_input())

        authenticated = cookie_authenticated or form_authenticated
        user = cookie_authenticated_user if cookie_authenticated else form_authenticated_user if form_authenticated else None

        return authenticated, user

    def check_cookie_authentication(self) -> Authentication:
        return NOT_AUTHENTICATED

    def _check_form_authentication(self, submit, username, password) -> Authentication:
        if not submit:
            return NOT_AUTHENTICATED
        return self._check_username_password(username, password)

    def _check_username_password(self, username, password) -> Authentication:
        found_user = self.user_source.load_by_username(username)
        if found_user is None or found_user.password != password:
            return NOT_AUTHENTICATED
        return True, found_user

    def _add_cookie(self):
        pass

    def _set_session_authentication_success(self):
        pass

    def _set_session_authentication_failed(self):
        pass
