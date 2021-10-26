import time


def wait_for_job():
    time.sleep(1.5)


def _print(content):
    print(content)
    wait_for_job()


class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]
