from subprocess import Popen, PIPE
from sys import executable


def install_pip_dependency(dependency):
    process = Popen([
        executable,
        "-m",
        "pip",
        "install",
        "--upgrade",
        dependency
    ], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()
    if process.returncode != 0:
        raise Exception(str(err))
