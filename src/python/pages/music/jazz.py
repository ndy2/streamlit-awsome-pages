import streamlit as st

from python.ui.page import Navigable, Drawable


class JazzNav(Navigable):
    _path = "music.jazz"
    name = "JAZZY"
    icon = "🎷"


class JazzDraw(Drawable):
    def draw(self):
        st.write("this is jazz page")


JazzDraw().draw()
