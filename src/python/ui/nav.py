from pathlib import Path
from typing import Dict

from streamlit.source_util import get_pages, _on_pages_changed
from streamlit.util import calc_md5

from python.ui.page import Navigable

StreamlitPages = Dict[str, Dict[str, str]]


def add_navs(
        *navs: Navigable
):
    pages = get_pages("")
    pages.clear()
    [add_nav(pages, nav) for nav in navs]


def add_nav(pages: StreamlitPages, nav: Navigable):
    script_path = Path(nav.relative_path)
    script_path_str = str(script_path.resolve())
    psh = calc_md5(script_path_str)
    pages[psh] = {
        "page_script_hash": psh,
        "page_name": nav.name,
        "icon": nav.icon,
        "script_path": script_path_str,
    }
    _on_pages_changed.send()
