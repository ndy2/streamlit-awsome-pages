import streamlit as st

from python.ui.page import Navigable, Drawable


class HelmNav(Navigable):
    _path = "study.helm"
    name = "Helm Helm"


class HelmDraw(Drawable):
    def _draw(self):
        1 / 0
        st.write("write your content here")


HelmDraw().draw()
