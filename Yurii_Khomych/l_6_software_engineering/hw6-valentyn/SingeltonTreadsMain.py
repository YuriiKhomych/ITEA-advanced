from threading import Thread, Lock


class SingletonMeta(type):
    _instance = None
    _lock: Lock = Lock()
    _count = 0

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__call__(*args, **kwargs)
                cls._count=+1

        return cls._instance


class Singleton(metaclass=SingletonMeta):
    value = None

    def __init__(self, value):
        self.value = value


    def some_business_logic(self):
        print(self._count)


def test_singleton(value):
    singleton = Singleton(value)
    singleton.some_business_logic()
    print(singleton.value)


if __name__ == "__main__":
    print("Starting some process:\n")

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()
