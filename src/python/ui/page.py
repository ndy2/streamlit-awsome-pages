import inspect
from abc import ABCMeta, abstractmethod

import streamlit as st

from python.auth.logout_ui import logout_sidebar


class Navigable(metaclass=ABCMeta):
    """
    Navigable is an abstract class that
        contains some properties which used for create sidebar navigation
    """

    @property
    @abstractmethod
    def path(self) -> str: pass

    @property
    @abstractmethod
    def name(self) -> str: pass

    @property
    def relative_path(self) -> str:
        return "src/python/pages/" + self.path.replace(".", "/") + ".py"

    @property
    def icon(self) -> str:
        return ""


class Drawable(metaclass=ABCMeta):
    """
    Drawable is an abstract class that
        wraps _draw in template method pattern manner
    """

    @abstractmethod
    def _draw(self):
        pass

    def draw(self):
        ## draw() should work only if user clicked its navigation in sidebar
        ## inspect.stack matches that scenario and prevent unintended invocation of draw by import page module
        if inspect.stack()[2][3] == '_run_script':
            st.markdown("<style>.css-8hkptd {  color: black !important; }</style>", unsafe_allow_html=True)
            logout_sidebar.draw()
            self._draw()
        return self


class Page(Navigable, Drawable, metaclass=ABCMeta):
    """
    Page = Navigable + Drawable
        recommendation - use it as singleton, instantiate it in same python file with itself
    """
    pass
