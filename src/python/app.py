from python.pages.home import HomePage
from python.pages.music import MusicSection
from python.pages.music.jazz import JazzPage
from python.pages.music.pop_song import PopSongPage
from python.pages.study import StudySection
from python.pages.study.helm import HelmPage
from python.pages.study.python import PythonPage
from python.ui.page_configurer import PageConfigurer

PageConfigurer() \
    .home_page(HomePage()) \
    .section(MusicSection(), [JazzPage(), PopSongPage()]) \
    .section(StudySection(), [PythonPage(), HelmPage()]) \
    .configure()
