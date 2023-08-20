import pathlib
import sys

sys.path.append(str(pathlib.Path().absolute()).split("/src")[0] + "/src")

import streamlit as st

from python.ui.page import Page


class PythonPage(Page):
    _path = "study.python"
    name = "Let's study python"
    icon = "👍"

    def draw(self):
        st.write("It's good!")


PythonPage().draw_with_nav_indent()
