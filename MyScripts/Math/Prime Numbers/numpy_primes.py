from array import array
from itertools import compress
from math import sqrt
import numpy as np
import time


def numpy_sieve1(n):
	"""Using numpy arrays."""
	
	A = np.ones((n + 1) // 2, dtype=np.bool)
	
	for i in range(3, int(sqrt(n)) + 1, 2):
		if A[i // 2]:
			A[i*i//2::i] = False
	
	return [2, *(2 * np.flatnonzero(A[1:]) + 3)]
	
def numpy_sieve2(n):
	"""Using method instead of function."""
	
	A = np.ones((n + 1) // 2, dtype=np.bool)
	
	for i in range(3, int(sqrt(n)) + 1, 2):
		if A[i // 2]:
			A[i*i//2::i] = False
	
	return [2, *(2 * A[1:].nonzero()[0] + 3)]

def numpy_sieve3(n, ones=np.ones, np_bool=np.bool, range=range, int=int, sqrt=sqrt, flatnonzero=np.flatnonzero):
	"""Passing global functions as arguments and not using keyword argument."""
	
	A = ones((n + 1) // 2, np_bool)
	
	for i in range(3, int(sqrt(n)) + 1, 2):
		if A[i // 2]:
			A[i*i//2::i] = False
	
	return [2, *(2 * flatnonzero(A[1:]) + 3)]

def numpy_sieve4(n, ones=np.ones, np_bool=np.bool, range=range, int=int, sqrt=sqrt, flatnonzero=np.flatnonzero):
	"""Using filter instead of if statement."""
	
	A = ones((n + 1) // 2, np_bool)
	
	for i in filter(lambda i: A[i // 2], range(3, int(sqrt(n)) + 1, 2)):
		A[i*i//2::i] = False
	
	return [2, *(2 * flatnonzero(A[1:]) + 3)]

functions = [numpy_sieve1, numpy_sieve2, numpy_sieve3, numpy_sieve4]

if __name__ == "__main__":
	for func in functions:
		print(f"{func.__doc__}")
		start = time.time()
		func(10000000)
		print(f"{func.__name__} took {time.time() - start} seconds.\n")
