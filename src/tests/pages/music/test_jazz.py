import playwright.sync_api

from python.pages.music import JazzPage
from test_support.base_test import BaseTestPage
from playwright.sync_api import expect

PlaywrightPage = playwright.sync_api.Page


class TestJazz(BaseTestPage):
    """
    cd $PROJECT_DIR; PYTHONPATH=src/ streamlit run src/python/music/jazz.py
    playwright codegen
    """
    sut = JazzPage()

    def test_draw(self):
        playwright_page: PlaywrightPage = self.playwright_page
        expect(playwright_page.get_by_text("this is jazz page")).to_be_visible()
        # expect(playwright_page.get_by_text("no occurence text")).to_be_visible()  <- fail
