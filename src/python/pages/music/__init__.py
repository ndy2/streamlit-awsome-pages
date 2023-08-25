from streamlit_extras.switch_page_button import switch_page

from python.ui.page import Page


class MusicSection(Page):
    _path = "music.__init__"
    name = "으막"
    icon = "🎵"

    def _draw(self):
        switch_page("JAZZY")


MusicSection().draw()
