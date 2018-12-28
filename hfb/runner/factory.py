from hfb.strategy import BaseBenchmarkStrategy, BaseBenchmarkResultStrategy
from hfb.strategy import BaseServerRunnerStrategy


class ApacheBench(BaseBenchmarkStrategy):
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


class Bombadier(BaseBenchmarkStrategy):
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


class PythonServerRunner(BaseServerRunnerStrategy):
    def run(self, *args, **kwargs):
        pass


class GunicornServerRunner(BaseServerRunnerStrategy):
    def run(self, *args, **kwargs):
        pass
