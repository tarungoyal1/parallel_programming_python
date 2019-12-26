import os
import threading


def task1(num):
	print("Task1 assigned to thread: {}".format(threading.current_thread().name))
	print("ID of process running task1: {}".format(os.getpid()))


def task2(num):
	print("Task2 assigned to thread: {}".format(threading.current_thread().name))
	print("ID of process running task2: {}".format(os.getpid()))


if __name__ == "__main__":

	print("ID of main process:{}".format(os.getpid()))
	print("Main thread name:{}".format(threading.main_thread().name))

	t1 = threading.Thread(target=task1, name='t1', args=(1,))
	t2 = threading.Thread(target=task2, name='t2', args=(2,))

	t1.start()
	t2.start()


	t1.join()
	t2.join()

	print("All done!")




