import streamlit as st

from python.ui.page import Page


class HelmPage(Page):
    _path = "study.helm"
    name = "Helm Helm"

    def _draw(self):
        1 / 0
        st.write("write your content here")


HelmPage().draw()
