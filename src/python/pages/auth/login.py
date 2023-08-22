import streamlit as st

from python.auth.authenticator import Authenticator
from python.pages.auth import app_authenticator
from python.ui.page import Navigable, Drawable


class LoginNav(Navigable):
    _path = "auth.login"
    name = "Login"
    icon = "🎷"


class _LoginUi:

    @staticmethod
    def login_form():
        login_form = st.form("Login")
        login_form.subheader("Login")

        username = login_form.text_input('Username').lower()
        password = login_form.text_input('Password', type='password')
        submit = login_form.form_submit_button('Login')

        return submit, username, password

    @staticmethod
    def authenticated_user(user):
        st.write("login successes")
        st.write(f"username : {user.username} ")
        st.write(f"age : {user.age} ")

    @staticmethod
    def authentication_failed():
        st.write("login failed!")


class LoginDraw(Drawable):

    def __init__(self, authenticator: Authenticator) -> None:
        super().__init__()
        self.authenticator = authenticator

    def draw(self):
        authenticated, user = self.authenticator.check_cookie_and_form_authentication(_LoginUi.login_form)
        if authenticated:
            _LoginUi.authenticated_user(user)
        else:
            _LoginUi.authentication_failed()


LoginDraw(app_authenticator).draw()
