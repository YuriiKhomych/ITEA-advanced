import time


# timer
class timer:
    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        pass

    def __exit__(self, *args):
        print("Time spent", time.time() - self.start)


with timer():
    time.sleep(2)
