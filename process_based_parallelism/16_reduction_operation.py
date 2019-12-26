from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD

rank = comm.rank

recvbuff = np.zeros(10, dtype=int)
sendbuff = (rank+1)*np.arange(10, dtype=int)

print("process ",rank," sending",sendbuff)

comm.Reduce(sendbuff, recvbuff, root=0, op=MPI.LAND)

if rank==0:
	print("On process ", rank, " after reduction:"," data=", recvbuff)

