from hfb.strategy import BaseBenchmarkStrategy, BaseBenchmarkResultStrategy
from hfb.strategy import BaseServerRunnerStrategy
from shutil import which
from hfb.utils import install_pip_dependency


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
    def _enter(self):
        return self

    def _exit(self, exc_type, exc_val, exc_tb):
        pass

    def run(self, *args, **kwargs):
        pass


class GunicornServerRunner(BaseServerRunnerStrategy):
    def _pre_enter(self):
        if not which("gunicorn"):
            install_pip_dependency("gunicorn")

    def _enter(self):
        return self

    def _exit(self, exc_type, exc_val, exc_tb):
        pass

    def run(self, *args, **kwargs):
        pass
