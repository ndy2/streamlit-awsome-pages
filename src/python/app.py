from python.pages.home import HomePage
from python.pages.music import MusicSection
from python.pages.music.jazz import JazzPage
from python.pages.music.pop_song import PopSongPage
from python.pages.study import StudySection
from python.pages.study.helm import HelmPage
from python.pages.study.python import PythonPage
from python.ui.util import add_navs_with_section

add_navs_with_section(
    HomePage(), {
        MusicSection(): [JazzPage(), PopSongPage()],
        StudySection(): [PythonPage(), HelmPage()],
    })
# add_navs(LoginNav())
