import os
import signal
import subprocess
from abc import ABCMeta, abstractmethod
from time import sleep

from playwright.sync_api import sync_playwright

from python.ui.page import Page


class BaseTestPage(metaclass=ABCMeta):
    @property
    @abstractmethod
    def sut(self) -> Page: pass

    @property
    def playwright_page(self) -> Page:
        return self._playwright_page

    def setup_method(self, method):
        command = self._get_streamlit_run_command(self.sut)
        print(f"[RUN SETUP COMMAND] {command}")
        self._process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            shell=True,
            preexec_fn=os.setsid
        )
        sleep(5)

        self._playwright = sync_playwright().start()
        self._browser = self._playwright.chromium.launch()
        self._context = self._browser.new_context()
        self._playwright_page = self._context.new_page()
        self._playwright_page.goto("http://localhost:8501/" + self.sut.name)

    def teardown_method(self, method):
        self._context.close()
        self._browser.close()
        self._playwright.stop()
        os.killpg(os.getpgid(self._process.pid), signal.SIGTERM)

    def _get_streamlit_run_command(self, sut: Page):
        cd = "cd " + "../.."
        streamlit_run = "streamlit run " + sut.relative_path
        return cd + "; " + streamlit_run
