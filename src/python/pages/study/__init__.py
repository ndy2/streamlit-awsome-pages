from streamlit_extras.switch_page_button import switch_page

from python.ui.page import Navigable, Drawable


class StudyNav(Navigable):
    _path = "study.__init__"
    name = "공부공부"
    icon = "📖"


class StudyDraw(Drawable):
    def _draw(self):
        switch_page("Let's study python")


StudyDraw().draw()
