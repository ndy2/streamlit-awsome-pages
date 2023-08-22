import streamlit as st

from python.ui.page import Navigable, Drawable


class PopSongNav(Navigable):
    _path = "music.pop_song"
    name = "PopSong"
    icon = "🎶"


class PopSongDraw(Drawable):
    def draw(self):
        st.write("this is pop_song page")


PopSongDraw().draw()
