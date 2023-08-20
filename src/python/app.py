import pathlib
import sys

sys.path.append(str(pathlib.Path().absolute()).split("/src")[0] + "/src")

from python.pages.home import Home
from python.pages.music.jazz import Jazz
from python.pages.music.pop_song import PopSong
from python.pages.study.helm import Helm
from python.pages.study.python import PythonPage
from python.ui.nav import draw_nav

draw_nav(
    Home(), {
        "🎵 Music": [Jazz(), PopSong()],
        "📖 Study Hard!": [Helm(), PythonPage()],
    }
)
