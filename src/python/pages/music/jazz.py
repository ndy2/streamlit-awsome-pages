import streamlit as st

from python.ui.page import Page


class JazzPage(Page):
    _path = "music.jazz"
    name = "JAZZY"

    def _draw(self):
        st.write("this is jazz page")


JazzPage().draw()
