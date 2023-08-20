import pathlib
import sys

sys.path.append(str(pathlib.Path().absolute()).split("/src")[0] + "/src")

import streamlit as st

from python.ui.page import Page


class PopSong(Page):
    _path = "music.pop_song"
    name = "PopSong"
    icon = "🎶"

    def draw(self):
        st.write("this is pop_song page")


PopSong().draw_with_nav_indent()
