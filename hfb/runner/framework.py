from hfb.strategy import AbstractFrameworkBenchmarkRunner
from hfb.strategy import BaseBenchmarkResultStrategy


class ApacheBenchRunner(AbstractFrameworkBenchmarkRunner):
    def _enter(self):
        return self

    def _exit(self, exc_type, exc_val, exc_tb):
        pass

    def run(self, *args, **kwargs):
        pass

    def report(self, *args, **kwargs):
        pass

    def result(self, *args, **kwargs) -> BaseBenchmarkResultStrategy:
        pass


class BombadierRunner(AbstractFrameworkBenchmarkRunner):
    def _enter(self):
        return self

    def _exit(self, exc_type, exc_val, exc_tb):
        pass

    def run(self, *args, **kwargs):
        pass

    def report(self, *args, **kwargs):
        pass

    def result(self, *args, **kwargs) -> BaseBenchmarkResultStrategy:
        pass
