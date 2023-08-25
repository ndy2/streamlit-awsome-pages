import streamlit as st

from python.ui.page import Page


class PopSongPage(Page):
    _path = "music.pop_song"
    name = "PopSong"

    def _draw(self):
        st.write("this is pop_song page")


PopSongPage().draw()
