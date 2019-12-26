import multiprocessing
import time

def worker(dictionary):
    for i in range(10):
        dictionary[i] = i**2
        time.sleep(1)


if __name__ == "__main__":
    mgr = multiprocessing.Manager()
    dictionary = mgr.dict()
    jobs = [multiprocessing.Process(target=worker, args=(dictionary, )) for _ in range(4)]

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    while True:
        print(dictionary)
        time.sleep(2)