from streamlit_extras.switch_page_button import switch_page

from python.pages.study.helm import HelmPage
from python.pages.study.python import PythonPage
from python.ui.page import Page


class StudySection(Page):
    _path = "study.__init__"
    name = "공부공부"
    icon = "📖"

    def _draw(self):
        switch_page("Let's study python")


study_section = StudySection()
study_section.draw()
