from mpi4py import MPI


comm = MPI.COMM_WORLD

rank = comm.rank

if rank ==0:
	data = [{"name":"Tarun", "age":"22", "interests":["Psychology", "Computer Science", "Physics"]}, {"name":"Rishabh", "age":"20", "interests":["Maths", "Physics"]}]
else:
	data = None

# Broadcast the data from rank=0 to all others
# you have to specify, root who is broadcasting the data in order to make other processes receive broadcasted data 
received_data = comm.bcast(data, root=0)

print("Rank: ", rank, ", Data received: ", received_data)


# Broadcast send the same data(array) to all other ranks
# while Scattering takes an data(array) and distributes contiguous sections of it across the ranks of a communicator. 
