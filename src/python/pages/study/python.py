import streamlit as st

from python.ui.page import Page


class PythonPage(Page):
    _path = "study.python"
    name = "Let's study python"

    def _draw(self):
        st.write("It's good!")


PythonPage().draw()
