import time
import multiprocessing

def task():
	print("Called by process:", multiprocessing.Process().name)




class MyProcess(multiprocessing.Process):
	def  __init__(self, tgt):
		multiprocessing.Process.__init__(self, target = tgt)

	# run() method is given more priority, and called when start() is invoked
	# def run(self):
	# 	print("called run method in: ", self.name)


if __name__ == "__main__":
	jobs = []

	for i in range(5):
		p = MyProcess(task)
		p.start()
			