import datetime
import time


class TimeWaster:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        time.sleep(2)
        result = self.function(self, *args, **kwargs)
        time.sleep(2)
        return result


@TimeWaster
def timer(self):
    print("Function is working: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


print("Time before the start: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
timer()
print("Time after the end: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
