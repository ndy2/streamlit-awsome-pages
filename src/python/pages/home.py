import pathlib
import sys

sys.path.append(str(pathlib.Path().absolute()).split("/src")[0] + "/src")

import streamlit as st

from python.ui.page import Page


class Home(Page):
    _path = "home"
    name = "Home Home"
    icon = "🏘"

    def draw(self):
        st.write("this is home page")


Home().draw()
