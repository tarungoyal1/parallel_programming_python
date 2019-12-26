from pyina.launchers import MpiPool, MpiScatter
import time

pool = MpiPool()

# this is fastest
jobs = MpiScatter()

def isPrime(n):
    if n%3==0:
        return False
    if n%5==0:
        return False
    if n%7==0:
        return False 

    i=5
    w=2
    while i*i<=n:
        if n%i==0:
            print(f"{n} is not prime")
            return False
        i +=w
        w=6-w
    print(f"{n} is prime")
    return True

start = time.time()
jobs.map(isPrime, range(3, 2000000, 2))
duration = time.time() - start
print("{:.2f} seconds".format(duration))