import inspect
from abc import ABCMeta, abstractmethod, ABC

import streamlit as st


class Navigable(metaclass=ABCMeta):

    @property
    @abstractmethod
    def _path(self): pass

    @property
    @abstractmethod
    def name(self): pass

    @property
    def relative_path(self):
        return "src/python/pages/" + self._path.replace(".", "/") + ".py"

    @property
    def icon(self):
        return ""


class Drawable(metaclass=ABCMeta):

    @abstractmethod
    def _draw(self):
        pass

    def draw(self):
        st.markdown("<style>.css-8hkptd {  color: black !important; }</style>", unsafe_allow_html=True)

        stack = inspect.stack()
        if stack[2][3] == '_run_script':
            self._draw()


class Page(Navigable, Drawable, ABC):
    pass
