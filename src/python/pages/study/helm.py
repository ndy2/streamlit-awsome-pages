import pathlib
import sys

sys.path.append(str(pathlib.Path().absolute()).split("/src")[0] + "/src")

import streamlit as st

from python.ui.page import Page


class Helm(Page):
    _path = "study.helm"
    name = "Helm Helm"
    icon = "❤️"

    def draw(self):
        st.write("write your content here")


Helm().draw_with_nav_indent()
