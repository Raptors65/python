import itertools
import math

def wheel_factorization(n):
	# Making the sieve array.
	A = [True] * (n + 1)
	# Storing the precalculated wheel.
	wheel = [2, 4]
	# Variable to store the iteration index.
	wheel_index = 0
	# Variable to store the current number being tested.
	i = 5
	
	# Looping until the sqrt of n.
	while i <= math.sqrt(n):
		# Checking if i is prime.
		if A[i]:
			# Crossing out multiples of i.
			A[i*i::i] = [False] * (((n+1)-i*i-1)//i+1)
		# Incrementing i by the current number on the wheel.
		i += wheel[wheel_index % len(wheel)]
		# Incrementing the iteration index.
		wheel_index += 1
	# Resetting variables (to get ready for another loop through the list).
	wheel_index = 0
	i = 5
	# Looping until n.
	while i <= n:
		# Checking if i is prime.
		if A[i]:
			# Yielding the prime number.
			yield i
		# Incrementing i by the current number on the wheel.
		i += wheel[wheel_index % len(wheel)]
		# Incrementing the iteration index.
		wheel_index += 1



def segmented_sieve(n):
	SEGMENT_SIZE = 10
	multiples = {}
	
	i = 2
	for start in range(2, n + 1, SEGMENT_SIZE):
		stop = min(start + SEGMENT_SIZE - 1, n)
		
		while i <= stop:
			if i not in multiples.values():
				multiples.update(((i, i*i),),)
				yield i
			else:
				while i in multiples.values():
					print(multiples, i)
					prime = list(multiples.keys())[list(multiples.values()).index(i)]
					multiples[prime] += prime
					print(multiples)
			i += 1
