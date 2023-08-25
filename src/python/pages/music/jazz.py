import streamlit as st

from python.ui.page import Navigable, Drawable


class JazzNav(Navigable):
    _path = "music.jazz"
    name = "JAZZY"


class JazzDraw(Drawable):
    def _draw(self):
        st.write("this is jazz page")


JazzDraw().draw()
