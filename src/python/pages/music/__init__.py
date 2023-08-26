from streamlit_extras.switch_page_button import switch_page

from python.pages.music.jazz import JazzPage, jazz_page
from python.pages.music.pop_song import PopSongPage, pop_song_page
from python.ui.page import Page


class MusicSection(Page):
    _path = "music.__init__"
    name = "으막"
    icon = "🎵"

    def _draw(self):
        switch_page("JAZZY")


music_section = MusicSection()
music_section.draw()
music_section_with_subpages = music_section, [jazz_page, pop_song_page]
