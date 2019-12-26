from threading import Thread, current_thread

def task1():
	print("in module, task1 assigned to :{}".format(current_thread().name))

class CookThread(Thread):
	def __init__(self, target):
		Thread.__init__(self, target=target)

	# if you don't pass callable object as argument to initializer (Thread.__init__(self, target=target))
	# then override the run method in subclass here because without overriding, start() will call run() implemented in base class

	# def run():
	# 	pass

if __name__ == '__main__':
	ct = CookThread(target=task1)
	ct.start()
	ct.join()