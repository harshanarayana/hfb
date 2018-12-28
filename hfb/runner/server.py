from os import kill
from shutil import which
from signal import SIGTERM
from subprocess import Popen, PIPE
from sys import executable

from hfb.exception import MissingConfigurationException
from hfb.strategy import AbstractServerRunner
from hfb.utils import install_pip_dependency
from hfb.utils import substitute_path_macros, extract_server_runner_args


class PythonServerRunner(AbstractServerRunner):
    def _enter(self):
        try:
            if not self.get_run_command():
                raise MissingConfigurationException("Missing parameter run_command")
            extract_server_runner_args(self)
        except AttributeError as e:
            raise MissingConfigurationException("Missing parameter run_command")

        return self

    def _exit(self, exc_type, exc_val, exc_tb):
        pid = self._server_process.pid
        kill(pid, SIGTERM)

    def run(self, *args, **kwargs):
        command = [executable, substitute_path_macros(self.get_run_command())]
        self._server_process = Popen(
            command, stderr=PIPE, stdout=PIPE, stdin=PIPE, close_fds=True
        )


class GunicornServerRunner(AbstractServerRunner):
    def _pre_enter(self):
        if not which("gunicorn"):
            install_pip_dependency("gunicorn")

    def _enter(self):
        try:
            if not self.get_run_command():
                raise MissingConfigurationException("Missing parameter run_command")
            extract_server_runner_args(self)
        except AttributeError as e:
            raise MissingConfigurationException("Missing parameter run_command")

        return self

    def _exit(self, exc_type, exc_val, exc_tb):
        pid = self._server_process.pid
        kill(pid, SIGTERM)

    def run(self, *args, **kwargs):
        command = ["gunicorn", substitute_path_macros(self.get_run_command())]
        self._server_process = Popen(
            command, stderr=PIPE, stdout=PIPE, stdin=PIPE, close_fds=True
        )
