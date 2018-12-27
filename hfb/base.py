from abc import ABCMeta, abstractmethod
from loguru import logger


# noinspection PyShadowingNames
class BaseBenchmarkRunner(metaclass=ABCMeta):
    def __init__(self, server, **kwargs):
        self._server = server
        self._init_additional_properties(**kwargs)

    def __enter__(self):
        try:
            return self._enter()
        except AttributeError as e:
            logger.warning("No valid implementation for _enter method found")
            raise e

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self._exit()
        except AttributeError as e:
            logger.warning("No valid implementation for _exit method found")
            raise e

    def _init_additional_properties(self, **kwargs):
        for p, v in kwargs.items():
            self.add_property(type(v), p)
            _setter = getattr(self, "set_{}".format(p))
            _setter(v)

    def _add_method(self, prop_type: type, prop_name: str):
        def _setter(self, value):
            try:
                if isinstance(value, prop_type):
                    setattr(self, prop_name, value)
                else:
                    raise TypeError("Invalid type {} for property {}".format(type(value), prop_name))
            finally:
                pass

        def _getter(self):
            return getattr(self, prop_name)

        setattr(self.__class__, "get_{}".format(prop_name), _getter)
        setattr(self.__class__, "set_{}".format(prop_name), _setter)

    def add_property(self, prop_type: type, prop_name: str):
        self._add_method(prop_type=prop_type, prop_name=prop_name)

    @property
    def server(self):
        return self._server

    @server.setter
    def server(self, server):
        self._server = server

