from abc import ABCMeta, abstractmethod


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


class Drawable(metaclass=ABCMeta):

    @abstractmethod
    def draw(self):
        pass
