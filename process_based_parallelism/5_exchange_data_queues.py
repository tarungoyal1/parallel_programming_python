from multiprocessing import Process, Queue
import time
import random
import gc

class Producer(Process):

	def __init__(self, queue, name):
		Process.__init__(self)
		self.queue = queue
		self.name = name

	def run(self):
		for i in range(5):
			item = random.randint(0, 256)
			self.queue.put(item)
			print("Producer process:",self.name," pushed item: ", item)
			print("Queue size: ", self.queue.qsize())
			time.sleep(1)

class Consumer(Process):

	def __init__(self, queue, name):
		Process.__init__(self)
		self.queue = queue
		self.name = name

	def run(self):
		try:
			while True:
				if self.queue.empty():
					# print("Queue is empty")
					break
				else:
					item = self.queue.get()
					for i in item:
						print(i)
						# time.sleep(1)
						# print("------")
					# print("Consumer process:",self.name," popped item: ", item)
					
		except KeyboardInterrupt as e:
			print(str(e))

if __name__ == "__main__":

	queue = Queue()

	for i in range(1000):
		slice = [x for x in range(i*2000, (i+1)*2000)]
		queue.put(slice)

	# for i in range(10000):
	# 	queue.put(i)top

	# pro1 = Producer(queue, name="Producer 1")
	# pro1.start()

	# here 4 consumers will run parallel
	start = time.time()

	jobs = []
	for i in range(4):
		cons = Consumer(queue, name="Consumer "+str(1))
		jobs.append(cons)

	for j in jobs:
		j.start()

	for j in jobs:
		j.join()



	duration = time.time() - start
	print("{:.2f} seconds".format(duration))
	gc.collect()