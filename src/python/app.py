from python.pages.auth.login import LoginNav
from python.pages.home import HomeNav
from python.pages.music.jazz import JazzNav
from python.pages.music.pop_song import PopSongNav
from python.pages.study.helm import HelmNav
from python.pages.study.python import PythonNav
from python.ui.nav import add_navs

add_navs(
    LoginNav(),
    HomeNav(),
    JazzNav(),
    PopSongNav(),
    HelmNav(),
    PythonNav()
)
