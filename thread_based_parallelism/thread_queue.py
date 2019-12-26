from threading import Thread
from queue import Queue
import time
import random


class producer(Thread):

	def __init__(self, queue):
		Thread.__init__(self)
		self.queue = queue

	def run(self):
		for _ in range(10):
			item = random.randint(0, 256)
			self.queue.put(item)
			print("Producer notify: item "+str(item)+" appended to queue by "+self.name)
			time.sleep(4)

class consumer(Thread):

	def __init__(self, queue):
		Thread.__init__(self)
		self.queue = queue

	def run(self):
		while True:
			item = self.queue.get()
			print("Consumer notify: item "+str(item)+" popped from queue by "+self.name+"\n")
			self.queue.task_done()

if __name__ == "__main__":

	queue = Queue()
	t1 = producer(queue)
	t2 = consumer(queue)
	t3 = consumer(queue)

	t1.start()
	t2.start()
	t3.start()

	t1.join()
	t2.join()
	t3.join()