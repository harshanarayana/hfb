from subprocess import Popen, PIPE
from sys import executable
from os import getcwd
from os import path
from hfb.strategy import AbstractServerRunner


def install_pip_dependency(dependency):
    process = Popen(
        [executable, "-m", "pip", "install", "--upgrade", dependency],
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
    )
    out, err = process.communicate()
    if process.returncode != 0:
        raise Exception(str(err))


def substitute_path_macros(path_value):
    if isinstance(path_value, str):
        return path_value.format(cwd=path.abspath(getcwd()), home=path.expanduser("~"))
    elif isinstance(path_value, (list, tuple)):
        for index, _ in enumerate(path_value):
            path_value[index] = path_value[index].format(
                cwd=path.abspath(getcwd()), home=path.expanduser("~")
            )
        return path_value


def enhance_server_run_command(runner: AbstractServerRunner, additional_params):
    old_command = runner.get_run_command()
    try:
        command = runner.get_run_command()
        if isinstance(command, str):
            command = [command]

        if isinstance(additional_params, (list, tuple)):
            command = command + additional_params
        else:
            command.append(additional_params)
        runner.set_run_command(command)
    except:
        runner.set_run_command(old_command)


def extract_server_runner_args(runner: AbstractServerRunner):
    try:
        args = runner.get_run_args()
        if isinstance(args, dict):
            args = ["{}={}".format(k, v) for k, v in args]
        enhance_server_run_command(runner, args)
    except:
        pass
