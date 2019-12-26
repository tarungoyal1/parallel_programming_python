from multiprocessing import Pool
from multiprocessing import freeze_support
import time
import concurrent.futures

'''Define function to run mutiple processors and pool the results together'''
def run_multiprocessing(func, i, n_processors):
    with Pool(processes=n_processors) as pool:
        return pool.map(func, i)

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

def fun(l):
	for i in l:
		print(i)



freeze_support()   # required to use multiprocessing

nums = [[x for x in range(i*2000, (i+1)*2000)] for i in range(1000)]
# print(nums[:5])

start = time.time()

# with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
#     executor.map(isPrime, nums)

run_multiprocessing(fun, nums, 4)

duration = time.time() - start
print(f"{duration:.2f} seconds")
