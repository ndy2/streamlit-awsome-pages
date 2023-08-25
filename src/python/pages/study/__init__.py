from streamlit_extras.switch_page_button import switch_page

from python.ui.page import Page


class StudySection(Page):
    _path = "study.__init__"
    name = "공부공부"
    icon = "📖"

    def _draw(self):
        switch_page("Let's study python")


StudySection().draw()
