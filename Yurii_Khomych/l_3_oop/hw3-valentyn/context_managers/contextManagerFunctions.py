from contextlib import contextmanager


C = 3


@contextmanager
def single():
    print("Starting", C)
    yield ()
    print("Finishing", C)


context = single()
with context:
    C = 19
    print("C = ", C)
