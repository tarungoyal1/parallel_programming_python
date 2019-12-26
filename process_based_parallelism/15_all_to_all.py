from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.Get_size()

sendbuf = (rank+1)*np.arange(size, dtype=int)
recvbuf = np.empty(size*1,dtype=int)

comm.Alltoall(sendbuf, recvbuf)
print("process ", rank, " sending ", sendbuf, " receiving ", recvbuf)