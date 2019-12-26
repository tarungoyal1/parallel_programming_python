import multiprocessing

def foo():
	print("Starting function:")
	time.sleep(3)
	print("Exiting process:")



if __name__ == "__main__":
	p = multiprocessing.Process(target=foo)
	print("Process before execution:", p, p.is_alive())

	p.start()
	print("Process running:", p, p.is_alive())


	p.terminate()
	print("Process terminated:", p, p.is_alive())

	p.join()
	print("Process joined:", p, p.is_alive())