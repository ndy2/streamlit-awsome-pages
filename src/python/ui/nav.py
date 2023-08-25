from pathlib import Path
from typing import Dict

from streamlit.source_util import get_pages, _on_pages_changed
from streamlit.util import calc_md5

from python.ui.page import Navigable

StreamlitPages = Dict[str, Dict[str, str]]


def add_navs_with_section(
        home_nav: Navigable,
        sections: dict[Navigable, list[Navigable]]
):
    pages = get_pages("")
    pages.clear()
    add_nav(pages, home_nav, "")
    for section_nav, navs in sections.items():
        add_nav(pages, section_nav, section_nav.icon)
        for nav in navs[:-1]:
            add_nav(pages, nav, "├")
        add_nav(pages, navs[-1], "└")
    _on_pages_changed.send()


def add_nav(pages: StreamlitPages, nav: Navigable, icon: str):
    script_path = Path(nav.relative_path)
    script_path_str = str(script_path.resolve())
    page_script_hash = calc_md5(script_path_str)
    pages[page_script_hash] = {
        "page_script_hash": page_script_hash,
        "page_name": nav.name,
        "icon": icon,
        "script_path": script_path_str,
    }
