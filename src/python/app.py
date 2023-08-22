import pathlib
import sys

from python.pages.music.jazz import JazzNav
from python.pages.music.pop_song import PopSongNav
from python.pages.study.helm import HelmNav
from python.pages.study.python import PythonNav
from python.ui.nav import add_navs

sys.path.append(str(pathlib.Path().absolute()).split("/src")[0] + "/src")

from python.pages.home import HomeNav

add_navs(
    HomeNav(),
    JazzNav(),
    PopSongNav(),
    HelmNav(),
    PythonNav()
)
