import streamlit as st

from python.ui.page import Navigable, Drawable


class PythonNav(Navigable):
    _path = "study.python"
    name = "Let's study python"


class PythonDraw(Drawable):

    def _draw(self):
        st.write("It's good!")


PythonDraw().draw()
