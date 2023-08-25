import streamlit as st

from python.ui.page import Navigable, Drawable


class PopSongNav(Navigable):
    _path = "music.pop_song"
    name = "PopSong"


class PopSongDraw(Drawable):
    def _draw(self):
        st.write("this is pop_song page")


PopSongDraw().draw()
