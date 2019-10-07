class Foo:
    pass

f = Foo()

def new(cls):
    x = object.__new__(cls)
    x.attr = 100
    return x

def init(self, ):
    self.new_attr = 200

Foo.__init__ = init

Foo.__new__ = new

f1 = Foo()
f1.attr


g = Foo()
g.attr