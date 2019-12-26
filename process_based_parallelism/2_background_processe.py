import multiprocessing
import time
import sys

def foo_non_daemon():
	name = multiprocessing.current_process().name
	print("Starting process:", name)
	print("Exiting process:", name)

def foo_daemon():
	name = multiprocessing.current_process().name
	print("Starting process:", name)
	time.sleep(3)
	print("Exiting process:", name)



if __name__ == "__main__":
	background_process = multiprocessing.Process(target=foo_daemon, name="Background_process")
	background_process.daemon = True

	no_background_process = multiprocessing.Process(target=foo_non_daemon, name="No_Background_process")

	background_process.start()
	no_background_process.start()

	# use this to tell main process for wait till daemonic process completes
	# background_process.join()

	no_background_process.join()
	# if you don't use join() on daemonic process then
	# it will even end the main program and therefore the daemon process without its completion
	# print(sys.version)


# Running a process in background
# they are useful when the process going on doesn't need your intervention (e.g. heartbeat)

# if daemon field is set to True, it becomes a background process

# background process(daemonic process) ends as the main process(program) exits means
# main process doesn't wait for it unless you have used join() for it

# it is not allowed to create child processes because it would leave its children orphaned
# because it would have terminated with the main process(program)






