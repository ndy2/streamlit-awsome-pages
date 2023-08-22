
import streamlit as st

from python.ui.page import Navigable, Drawable


class PythonNav(Navigable):
    _path = "study.python"
    name = "Let's study python"
    icon = "👍"

class PythonDraw(Drawable):

    def draw(self):
        st.write("It's good!")


Drawable().draw()
