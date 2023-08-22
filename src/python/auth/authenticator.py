from typing import Optional

import extra_streamlit_components as stx

from python.auth.domain import User, UserSource

Authentication = tuple[bool, Optional[User]]


class Authenticator:

    def __init__(self, user_source: UserSource) -> None:
        super().__init__()
        self.user_source = user_source
        self.cookie_manager = stx.CookieManager()

    def check_cookie_and_form_authentication(self, login_form_with_input) -> Authentication:
        pass

    def check_cookie_authentication(self) -> Authentication:
        return False, None

    def _check_form_authentication(self) -> Authentication:
        pass

    def _add_cookie(self):
        pass

    def _set_session_authentication_success(self):
        pass

    def _set_session_authentication_failed(self):
        pass
