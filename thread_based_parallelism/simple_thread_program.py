from threading import Thread


def task1(n):
	print("Task1 started")
	print("Cube (in task1):"+str(n*n*n))
	print("Task2 ended")

def task2(n):
	print("Task2 started")
	print("Square (in task2):"+str(n*n))


if __name__ == "__main__":
	t1 = Thread(target=task1, args=(7,))
	t2 = Thread(target=task2, args=(7,))

	t1.start()
	t2.start()

	# join() tells means main program has to wait until task is finished in thread 
	t1.join()
	t2.join()

	print("Ending of main program")
