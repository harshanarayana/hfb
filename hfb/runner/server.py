from hfb.strategy import AbstractServerRunner
from shutil import which
from hfb.utils import install_pip_dependency


class PythonServerRunner(AbstractServerRunner):
    def _enter(self):
        return self

    def _exit(self, exc_type, exc_val, exc_tb):
        pass

    def run(self, *args, **kwargs):
        pass


class GunicornServerRunner(AbstractServerRunner):
    def _pre_enter(self):
        if not which("gunicorn"):
            install_pip_dependency("gunicorn")

    def _enter(self):
        return self

    def _exit(self, exc_type, exc_val, exc_tb):
        pass

    def run(self, *args, **kwargs):
        pass
