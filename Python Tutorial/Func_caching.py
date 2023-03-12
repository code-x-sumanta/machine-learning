import time
from functools import lru_cache

@lru_cache(maxsize=20)

def some_work(n):
    # some task taking n seconds
    time.sleep(n)
    return n

if __name__=="__main__":
    print("Now running few second....")
    some_work(3)
    some_work(4)
    some_work(2)
    some_work(5)
    print("Work done...Calling again")
    some_work(3)
    print("Called again")