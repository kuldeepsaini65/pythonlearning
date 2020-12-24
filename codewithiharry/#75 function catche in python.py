from time import sleep
from functools import lru_cache


@lru_cache(maxsize=1)
def time_loader(seconds):
    sleep(seconds)
    return seconds


if __name__ == "__main__":
    time_loader(3)
    print("Loaded Complete 1st Time")
    time_loader(3)
    print("Done 2nd time")
    time_loader(3)
    print("done 3rd time")
