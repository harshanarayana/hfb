from hfb.strategy import BaseBenchmarkStrategy, BaseServerRunnerStrategy
import hfb.runner.factory
from inspect import getmembers


class Context:
    def __init__(self, benchmark_runner: BaseBenchmarkStrategy, server_runner: BaseServerRunnerStrategy):
        self._benchmark_runner = benchmark_runner
        self._server_runner = server_runner

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._benchmark_runner.report()

    def benchmark(self, *args, **kwargs):
        with self._server_runner as server:
            server.run(*args, **kwargs)
            with self._benchmark_runner as strategy:
                strategy.run(*args, **kwargs)

    def report(self, *args, **kwargs):
        return self._benchmark_runner.report(*args, **kwargs)

    @classmethod
    def strategy(cls, benchmark_strategy: str, server_strategy: str, *args, **kwargs):
        return cls(
            get_runner(benchmark_strategy, *args, **kwargs),
            get_runner(server_strategy, *args, **kwargs))


def get_runner(strategy:str = "ApacheBench", *args, **kwargs):
    if not list(filter(lambda member: strategy == member[0], getmembers(factory))):
        raise NotImplementedError("Missing Benchmark Runner Strategy for: {}".format(strategy))
    klass = getattr(factory, strategy)
    return klass(*args, **kwargs)


def register_runner(strategy):
    setattr(factory, strategy.__name__, strategy)
