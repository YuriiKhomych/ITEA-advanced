from abc import ABCMeta, abstractmethod, abstractclassmethod, abstractstaticmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class Concrete(Base):
    def foo(self):
        pass

    def bar(self):
        pass


c = Concrete()
