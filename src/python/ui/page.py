from abc import *

from st_pages import add_indentation


class Drawable(metaclass=ABCMeta):

    @abstractmethod
    def draw(self):
        pass


class Navigable(metaclass=ABCMeta):

    @property
    def relative_path(self):
        return "src/python/pages/" + self._path.replace(".", "/") + ".py"

    @property
    @abstractmethod
    def _path(self): pass

    @property
    @abstractmethod
    def name(self): pass

    @property
    @abstractmethod
    def icon(self): pass


class Page(Drawable, Navigable, metaclass=ABCMeta):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Page, cls).__new__(cls, *args, **kwargs)

        return cls._instance

    def draw_with_nav_indent(self):
        add_indentation()
        self.draw()
