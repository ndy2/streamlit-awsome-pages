from streamlit_extras.switch_page_button import switch_page

from python.ui.page import Navigable, Drawable


class MusicNav(Navigable):
    _path = "music.__init__"
    name = "으막"
    icon = "🎵"


class MusicDraw(Drawable):
    def _draw(self):
        switch_page("JAZZY")


MusicDraw().draw()
