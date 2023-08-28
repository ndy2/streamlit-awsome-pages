import streamlit as st

from python.ui.page import Page


class PythonPage(Page):
    path = "study.python"
    name = "Let's study python"

    def _draw(self):
        st.write("It's good!")


python_page = PythonPage().draw()
