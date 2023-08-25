from python.pages.home import HomeNav
from python.pages.music import MusicNav
from python.pages.music.jazz import JazzNav
from python.pages.music.pop_song import PopSongNav
from python.pages.study import StudyNav
from python.pages.study.helm import HelmNav
from python.pages.study.python import PythonNav
from python.ui.nav import add_navs_with_section

# add_navs(
#     HomeNav(),
#     LoginNav(),
#     JazzNav(),
#     PopSongNav(),
#     HelmNav(),
#     PythonNav()
# )

add_navs_with_section(
    HomeNav(), {
        MusicNav(): [JazzNav(), PopSongNav()],
        StudyNav(): [PythonNav(), HelmNav()],
    })
# add_navs(LoginNav())
