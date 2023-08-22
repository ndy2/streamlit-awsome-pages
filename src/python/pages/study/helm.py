import streamlit as st

from python.ui.page import Navigable, Drawable


class HelmNav(Navigable):
    _path = "study.helm"
    name = "Helm Helm"
    icon = "❤️"


class HelmDraw(Drawable):
    def draw(self):
        st.write("write your content here")


HelmDraw().draw_with_nav_indent()
