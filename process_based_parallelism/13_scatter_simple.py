from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank


if rank==0:
	data = [[x for x in range(10)] for x in range(4)] 
else:
	data = None

# scatter() (note: small s) recieves only data and root as args and returns the recv buffer

recvbuf = comm.scatter(data,root=0)

print("Rank: ",rank," Received data: ", recvbuf)