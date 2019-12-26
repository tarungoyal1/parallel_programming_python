from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size() # gives number of ranks in comm
rank = comm.rank


if rank==0:
	# size = 4 (-n 4)
	# create a list containing 4 lists containing with each 0 to 3 nums 10 times
	# [
	# 	    [0 0 0 0 0 0 0 0 0 0]                                                                                       
 	# 		[1 1 1 1 1 1 1 1 1 1]                                                                                       
 	# 		[2 2 2 2 2 2 2 2 2 2]                                                                                       
 	# 		[3 3 3 3 3 3 3 3 3 3]
 	# 	]  
 	# each list is given to each process, rankwise means 0th list goes to 0th ranked process and so on


	data = np.empty([size, 10], dtype='i')
	data.T[,:] = range(size)
	print(data)
else:
	# to initialize data=None for ranks other than rank=0,
	# because only rank=0 is sending(scattering) data to others including itself
	# and others are only receiving the chunked(a single list) data
	data = None


recvbuf = np.empty(10, dtype='i')

comm.Scatter(data,recvbuf,root=0)

print("Rank: ",rank," Received data: ", recvbuf)