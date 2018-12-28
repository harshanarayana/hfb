from hfb.strategy import BaseBenchmarkStrategy
import hfb.runner.factory
from inspect import getmembers


class Context:
    def __init__(self, runner: BaseBenchmarkStrategy):
        self._runner = runner

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._runner.report()

    def benchmark(self, *args, **kwargs):
        with self._runner as strategy:
            strategy.run(*args, **kwargs)

    def report(self, *args, **kwargs):
        return self._runner.report(*args, **kwargs)

    @classmethod
    def strategy(cls, strategy: str, *args, **kwargs):
        return cls(get_runner(strategy, *args, **kwargs))


def get_runner(strategy:str = "ApacheBench", *args, **kwargs):
    if not list(filter(lambda member: strategy == member[0], getmembers(factory))):
        raise NotImplementedError("Missing Benchmark Runner Strategy for: {}".format(strategy))
    klass = getattr(factory, strategy)
    return klass(*args, **kwargs)


def register_runner(strategy):
    setattr(factory, strategy.__name__, strategy)
