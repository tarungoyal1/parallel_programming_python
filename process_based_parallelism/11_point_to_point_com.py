from mpi4py import MPI
import time

#  default communicator, this is used to communicate among processes
comm = MPI.COMM_WORLD

rank = comm.rank
print('My rank: ',rank)

# this is point to point communication, you can send data from 1 source to 1 destination
if rank==0:
	# you can send anything, i am sending a dictionary
	data = {'a': 7, 'b': 3.14}
	destination = 3
	comm.send(data, dest=destination)
	time.sleep(1) #just for demo
	print("sending data:",data," from process:",rank,"to process:", destination)


if rank==3:
	# you must specify the source to recieve the data
	data = comm.recv(source=0)
	print("received data:",data," by process:", 3)

# another example, here we send a string saying 'hello'
if rank==1:
	data = "Hello"
	destination = 2
	comm.send(data, dest=destination)
	time.sleep(1)#just for demo
	print("sending data:",data," from process:",rank,"to process:", destination)

if rank==2:
	data = comm.recv(source=1)
	print("received data:",data," by process:", 1)

#mpirun -n 4 python filename.py 

# Here the -n 4 tells MPI to use four processes, which is the number of cores I have on my laptop. Then we tell MPI to run the python script named script.py.
# If you are running this on a desktop computer, then you should adjust the -n argument to be the number of cores on your system or the maximum number of processes needed for your job, whichever is smaller. Or on a large cluster you would specify the number of cores that your program needs or the maximum number of cores available on the particular cluster.

#each process run same compiled binary of this script