from loguru import logger
from hfb.strategy.base import BaseBenchmarkStrategy
from pytest import raises
import sys

logger.remove(0)
logger.add(sys.stderr, colorize=True, format="<green>{time:YY:MM:DD HH:MM}</green> <level>{message}</level>")


class TestBenchmarkStrategy(BaseBenchmarkStrategy):
    def run(self, *args, **kwargs):
        pass

    def report(self, *args, **kwargs):
        pass

    def result(self, *args, **kwargs):
        pass


class TestBaseBenchmarkRunner:

    def test_default_init_with_no_args(self):
        logger.info("Testing default Base class with No Additional Args")
        base = TestBenchmarkStrategy(server="sanic")
        assert base.server == "sanic"

    def test_base_with_additional_param(self):
        logger.info("Testing default base class with Additional arguments")
        base = TestBenchmarkStrategy(server="sanic", p1="v1", p2=True, p3=BaseBenchmarkStrategy)
        assert getattr(base, "get_p1")
        assert callable(getattr(base, "set_p1"))

    def test_base_with_additional_param_get_and_set(self):
        logger.info("Testing dynamically generated getter and setter methods")
        base = TestBenchmarkStrategy(server="sanic", p1="v1", p2=True, p3=BaseBenchmarkStrategy)
        assert base.get_p1() == "v1"

        with raises(expected_exception=TypeError) as e:
            base.set_p1(10)

        assert base.get_p2()
        base.set_p2(False)
        assert not base.get_p2()

        base.server = "TEST"
        assert base.server == "TEST"

    def test_missing_enter_and_exit_context_managers(self):
        logger.info("Testing Context Manager Methods")

        with raises(expected_exception=AttributeError) as e:
            with TestBenchmarkStrategy(server="test") as runner:
                runner.server = "other"

        class ExtendedBaseWithEnter(TestBenchmarkStrategy):
            def _enter(self):
                pass

        with raises(expected_exception=AttributeError) as e:
            with ExtendedBaseWithEnter(server="test") as s:
                s.server = "test"
            assert 1 == 1

    def test_context_manager_implementation(self):
        logger.info("Testing Base Benchmark Runner with Sample Context Provider")
        call_count = {
            "enter": 0,
            "exit": 0
        }

        class WithContext(TestBenchmarkStrategy):
            def __enter__(self):
                call_count["enter"] = 1
                return self

            def __exit__(self, exc_type, exc_val, exc_tb):
                call_count["exit"] = 1

        with WithContext(server="test") as s:
            assert s.server == "test"

        assert call_count["enter"] == 1
        assert call_count["exit"] == 1
