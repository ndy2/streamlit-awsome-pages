import streamlit as st

from python.ui.page import Navigable, Drawable


class HomeNav(Navigable):
    _path = "home"
    name = "Home Home"
    icon = "🏘"


class HomeDraw(Drawable):

    def draw(self):
        st.write("this is home page")


HomeDraw().draw()
