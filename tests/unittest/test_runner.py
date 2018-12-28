from pytest import raises
from loguru import logger
from hfb.runner import get_runner, register_runner, Context
from hfb.runner.factory import ApacheBench, BaseBenchmarkStrategy
from hfb.strategy import BaseBenchmarkResultStrategy
from hfb.strategy import BaseServerRunnerStrategy


class CustomStrategy(BaseBenchmarkStrategy):
    def run(self, *args, **kwargs):
        pass

    def report(self, *args, **kwargs):
        pass

    def result(self, *args, **kwargs) -> BaseBenchmarkResultStrategy:
        pass


class PyRunner(BaseServerRunnerStrategy):
    def _enter(self):
        return self

    def _exit(self, exc_type, exc_val, exc_tb):
        pass

    def run(self, *args, **kwargs):
        pass


class TestRunnerFactory:

    def test_get_runner_with_valid_strategy(self):
        logger.info("Testing get_runner with a valid registered strategy")
        strategy = get_runner("ApacheBench", server="test_server")
        assert isinstance(strategy, ApacheBench)
        assert strategy.server == "test_server"

    def test_get_runner_with_invalid_strategy(self):
        logger.info("Testing get_runner with an invalid runner strategy")
        with raises(expected_exception=NotImplementedError) as e:
            strategy = get_runner("MissingStrategy", server="missing")

    def test_dynamic_strategy_registration(self):
        logger.info("Testing custom strategy registration")
        register_runner(CustomStrategy)
        strategy = get_runner("CustomStrategy", server="custom")
        assert strategy.server == "custom"


class TestContext:

    def test_strategy_classmethod(self):
        register_runner(CustomStrategy)
        register_runner(PyRunner)
        with Context.strategy("CustomStrategy", "PyRunner", server="sanic") as context:
            assert isinstance(context._benchmark_runner, CustomStrategy)
            assert context._benchmark_runner.server == "sanic"

    def test_strategy_with_init(self):
        strategy = CustomStrategy(server="sanic")
        with Context(strategy, get_runner("PyRunner", server="sanic")) as context:
            assert isinstance(context._benchmark_runner, CustomStrategy)
            assert context._benchmark_runner.server == "sanic"

    def test_context_runner(self):
        call_count = {
            "run": 0,
            "report": 0,
            "result": 0,
            "_enter": 0,
            "_exit": 0
        }

        class TestStrategy(BaseBenchmarkStrategy):
            def run(self, *args, **kwargs):
                call_count["run"] = 1

            def report(self, *args, **kwargs):
                call_count["report"] = 1

            def result(self, *args, **kwargs) -> BaseBenchmarkResultStrategy:
                call_count["result"] = 1
                return BaseBenchmarkResultStrategy(server=self.server)

            def _enter(self):
                call_count["_enter"] = 1
                return self

            def _exit(self, exc_type, exc_val, exc_tb):
                call_count["_exit"] = 1
                pass

        register_runner(TestStrategy)

        with Context.strategy('TestStrategy', 'PyRunner', server="sanic") as context:
            context.benchmark()
            context.report()

        assert call_count["run"] == 1
        assert call_count["result"] == 0
        assert call_count["report"] == 1
        assert call_count["_enter"] == 1
        assert call_count["_exit"] == 1
