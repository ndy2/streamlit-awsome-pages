import pathlib
import sys

from python.ui.page import Navigable, Drawable

sys.path.append(str(pathlib.Path().absolute()).split("/src")[0] + "/src")

import streamlit as st



class HomeNav(Navigable):
    _path = "home"
    name = "Home Home"
    icon = "🏘"

class HomeDraw(Drawable):

    def draw(self):
        st.write("this is home page")


Home().draw()
