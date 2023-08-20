import st_pages

from python.ui.page import Page


def draw_nav(
        root_page: Page,
        section_page_dictionary: dict[str, list[Page]]
):
    nav = [_to_st_page(root_page, False)]
    for section, pages in section_page_dictionary.items():
        section_icon = section[0]
        section_name = section[2:]

        nav.append(st_pages.Section(section_name, section_icon))
        for page in pages:
            nav.append(_to_st_page(page, True))

    st_pages.show_pages(nav)


def _to_st_page(page: Page, in_section: bool) -> st_pages.Page:
    return st_pages.Page(
        page.relative_path,
        page.name,
        page.icon,
        in_section=in_section
    )
