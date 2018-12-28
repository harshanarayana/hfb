from hfb.strategy import BaseBenchmarkStrategy, BaseBenchmarkResultStrategy


class ApacheBench(BaseBenchmarkStrategy):
    def run(self, *args, **kwargs):
        pass

    def report(self, *args, **kwargs):
        pass

    def result(self, *args, **kwargs) -> BaseBenchmarkResultStrategy:
        pass


class Bombadier(BaseBenchmarkStrategy):
    def run(self, *args, **kwargs):
        pass

    def report(self, *args, **kwargs):
        pass

    def result(self, *args, **kwargs) -> BaseBenchmarkResultStrategy:
        pass
