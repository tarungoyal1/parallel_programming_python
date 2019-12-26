import multiprocessing
import time


def create_items(pipe):
	# output_pipe, _ = pipe
	for item in range(10):
		pipe[0].send(item)
		print("item:",item," sent through pipe1: ", time.time())
		time.sleep(3)
	# output_pipe.close()


def multiply_items(pipe1, pipe2):
	close, input_pipe = pipe1
	close.close()
	output_pipe, _ = pipe2
	try:
		while True:
			item = input_pipe.recv()
			print("item:",item," received from pipe1: ", time.time())
			output_pipe.send(item*item)
			print("item:",item," sent through pipe2: ", time.time())
	except Exception as e:
		print(str(e))


if __name__ == "__main__":

	pipe1 = multiprocessing.Pipe(True)
	process_pipe1 = multiprocessing.Process(target=create_items, args=(pipe1,))

	pipe2 = multiprocessing.Pipe(True)

	process_pipe2 = multiprocessing.Process(target=multiply_items, args=(pipe1, pipe2,))

	process_pipe1.start()
	process_pipe2.start()

	pipe1[0].close()
	pipe2[0].close()

	try:
		while True:
			item = pipe2[1].recv()
			print("item:",item," recieved from pipe2: ", time.time())
	except Exception as e:
		print(str(e))






