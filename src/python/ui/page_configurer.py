from pathlib import Path
from typing import Dict

from streamlit.source_util import get_pages
from streamlit.util import calc_md5
from streamlit_extras.switch_page_button import switch_page

from python.ui.page import Page

StreamlitPages = Dict[str, Dict[str, str]]


class PageConfigurer:

    def __init__(self) -> None:
        super().__init__()
        self._home_page = None
        self._streamlit_pages = get_pages("")
        self._streamlit_pages.clear()

    def home_page(self, page: Page) -> 'PageConfigurer':
        self._home_page = page
        self.page(page)
        return self

    def section(self, section: Page, sub_pages: list[Page]) -> 'PageConfigurer':
        self.page(section)
        for sub_page in sub_pages[:-1]:
            self.page(sub_page, "├")
        self.page(sub_pages[-1], "└")
        return self

    def page(self, page: Page, icon: str = "") -> 'PageConfigurer':
        page_icon = icon if icon != "" else page.icon
        script_path = Path(page.relative_path)
        script_path_str = str(script_path.resolve())
        page_script_hash = calc_md5(script_path_str)
        self._streamlit_pages[page_script_hash] = {
            "page_name": page.name,
            "icon": page_icon,
            "page_script_hash": page_script_hash,
            "script_path": script_path_str,
        }
        return self

    def configure(self) -> None:
        switch_page(self._home_page.name)
