from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.Get_size()

# writing here, each process(rank) is building data for itself while executing the script
data = (rank)**2

sendbuff = comm.gather(data, root=0)

# for rank=0 process which is receiving(gathering) the data

if rank==0:
	print("..receiving the data in rank:", rank) # will be 0
	print(sendbuff)
	for i in range(size):
		recvdata = sendbuff[i]
		print("Received data ",recvdata," from process", i)