from python.pages.auth.login import login_page
from python.pages.home import home_page
from python.pages.music import music_section_with_subpages
from python.pages.study import study_section
from python.pages.study.helm import helm_page
from python.pages.study.python import python_page
from python.ui.page_configurer import PageConfigurer

PageConfigurer() \
    .home_page(home_page) \
    .section(*music_section_with_subpages) \
    .section(study_section, [python_page, helm_page]) \
    .page(login_page) \
    .configure()
