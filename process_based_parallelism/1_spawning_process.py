import multiprocessing
import time

#best example to show how multiprocessing works

#here, each processes starts almost instantly as there is no join() method, and 
#within each calling target function, they all sharing(overlapping) sleep time of 10 seconds of each others
#not waiting for each to individually sleep for 10 seconds means they all sleep for 10 seconds in total simultaneously

# that's parallelism (5 people working/sleeping for 10 seconds simultaneously)

# Tip: is better to place task function in another script and import it from there
def function(i):
	print("function called from process:",i, time.time())
	time.sleep(10)
	print("work done by process:",i, time.time())



if __name__ == "__main__":
	jobs = []
	for i in range(10):
		p = multiprocessing.Process(target=function, args=(i, ))
		jobs.append(p)
		p.start()
	print(time.time())

