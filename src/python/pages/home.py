import streamlit as st

from python.ui.page import Page


class HomePage(Page):
    path = "home"
    name = "Home Home"

    def _draw(self):
        st.write("this is home page")


home_page = HomePage().draw()
