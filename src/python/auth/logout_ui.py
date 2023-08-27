import streamlit as st

from python.auth.authenticator import Authenticator


class _LogoutUi:

    @staticmethod
    def logout_button():
        return st.sidebar.button("logout")


class LogoutSideBar:

    def draw(self):
        if _LogoutUi.logout_button():
            Authenticator.logout()


logout_sidebar = LogoutSideBar()
