   # To use threads import Thread using the following code
from threading import Thread
from time import sleep

# To create a thread in python you need to make your class work as a thread
# For this, you should subclass your class from Thread class
class CookBook(Thread):

	def __init__(self):
		Thread.__init__(self)
		self.message = "Hello Parallel Python CookBook!"

	def print_message(self):
		print(self.message)

	def run(self):
		print("Thread starting\n")
		for i in range(10):
			self.print_message()
			sleep(2)
		print("Thread Ended!")


# Starting the process
print("Starting the main process")

hello_python = CookBook()


# Starting thread
hello_python.start()



# Ending the Process
print("Ending the main process")