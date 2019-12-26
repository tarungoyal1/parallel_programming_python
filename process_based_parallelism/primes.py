from mpi4py import MPI
import numpy as np
import more_itertools as mit
# import random
import time

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

def isPrime(n):
    if n%3==0:
        return False
    if n%5==0:
        return False
    if n%7==0:
        return False 

    i=5
    w=2
    while i*i<=n:
        if n%i==0:
            # print(f"{n} is not prime")
            return False
        i +=w
        w=6-w
    # print(f"{n} is prime")
    return True

start = time.time()

total = 1000000

numsPerRank = (total//size)
sub = numsPerRank-1

prank = rank+1

primes = np.arange((prank*numsPerRank)-sub, (prank*numsPerRank),2, dtype='i')
sendbuf = list(filter(isPrime, np.arange((prank*numsPerRank)-sub, (prank*numsPerRank),2, dtype=int)))
duration = time.time() - start
# # print('Rank: ',rank, ', sendbuf: ',sendbuf)

if rank==0:
	sendbuf.remove(1)
	sendbuf+=[2, 3, 5, 7]


print(sendbuf)
print(duration)

# if rank<size-1:
# 	data = duration
# 	destination = size-1
# 	comm.send(data, dest=destination)

# if rank == size-1:
# 	s = duration
# 	for i in range(size-1):
# 		s+=comm.recv(source=i)
# 		# print(data)
# 		# print("received data:",data," by process:", 3)
# 	print("{:.2f} seconds".format(s))
# print(sendbuf)
# data = [x for x in range((rank*sizePerRank)-subtractor, (rank*sizePerRank), 2)]
# primes = list(filter(isPrime, data))

# if rank == 0:
#     recvbuf = np.empty(shape=[4, 100])
#     print(recvbuf)
# else:
# 	recvbuf = None
# if rank == 1:
#     recvbuf = np.empty(4, dtype=int)
# else:
# 	recvbuf = None
# comm.Gatherv(sendbuf,(recvbuf, 40), root=1)

# if rank==1:
# 	print(recvbuf)
	# print("..receiving the data in rank:", rank) # will be 0
	# for i in range(4):
	# 	recvdata = recvbuf[i]
	# 	print("Received data ",recvdata," from process", i)

 

# numsPerRank = 10
# sub = numsPerRank-1 

# local_array = [rank] * random.randint(2, 5)
# print("rank: {}, local_array: {}".format(rank, local_array))

# sendbuf = np.array(local_array)

# primes = np.arange((rank*numsPerRank)-sub, (rank*numsPerRank),2, dtype='i')
# primes = list(filter(isPrime, np.arange((rank*numsPerRank)-sub, (rank*numsPerRank),2, dtype=int)))
# sendbuf = list(mit.padded(sendbuf, -1, numsPerRank))
# print(sendbuf)
# print('Rank: ',rank, ', sendbuf: ',sendbuf)
# sendcounts = np.array(comm.gather(len(sendbuf), root=1))

# if rank == 1:
#     print("sendcounts: {}, total: {}".format(sendcounts, sum(sendcounts)))
#     recvbuf = np.empty(sum(sendcounts), dtype=int)
# else:
# 	recvbuf = None

# comm.Gatherv(sendbuf=sendbuf, recvbuf=(recvbuf, sendcounts), root=1)

# if rank ==1:
# 	print(recvbuf)

# recvbuf = None
# if rank == 0:
#     recvbuf = np.empty(4, dtype='i')  

# comm.Gather(sendbuf, recvbuf, root=0)

# if rank == 0:
#     print('Rank: ',rank, ', recvbuf received: ',recvbuf)
