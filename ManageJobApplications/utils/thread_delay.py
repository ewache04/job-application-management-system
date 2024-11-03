import time


def thread_delay(value=None):
    if value is None:
        return time.sleep(1)
    else:
        return time.sleep(value)


