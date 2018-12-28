from abc import ABCMeta, abstractmethod

from hfb.strategy.base import _Base


class AbstractServerRunner(_Base, metaclass=ABCMeta):
    @abstractmethod
    def run(self, *args, **kwargs):
        """Implementation required"""
