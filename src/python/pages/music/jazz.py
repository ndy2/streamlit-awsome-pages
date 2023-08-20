import pathlib
import sys

sys.path.append(str(pathlib.Path().absolute()).split("/src")[0] + "/src")

import streamlit as st

from python.ui.page import Page


class Jazz(Page):
    _path = "music.jazz"
    name = "JAZZY"
    icon = "🎷"

    def draw(self):
        st.write("this is jazz page")


Jazz().draw_with_nav_indent()
