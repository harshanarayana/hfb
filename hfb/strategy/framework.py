from abc import ABCMeta, abstractmethod

from hfb.strategy.base import BaseBenchmarkResultStrategy
from hfb.strategy.base import _Base


class AbstractFrameworkBenchmarkRunner(_Base, metaclass=ABCMeta):
    @abstractmethod
    def run(self, *args, **kwargs):
        """Implementation required"""

    @abstractmethod
    def report(self, *args, **kwargs):
        """Implementation required"""

    @abstractmethod
    def result(self, *args, **kwargs) -> BaseBenchmarkResultStrategy:
        """Implementation required"""
