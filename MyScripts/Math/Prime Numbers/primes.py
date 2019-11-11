from itertools import compress
from array import array
from math import sqrt
import numpy as np
from timeit import timeit

def sieve(n):
	"""Simple sieve."""
	
	A = [True] * (n + 1)
	
	for i in range(2, int(sqrt(n)) + 1):
		if A[i]:
			A[i*i::i] = [False] * (((n+1)-i*i-1)//i+1)
	
	return list(compress(range(2, n + 1), A[2:]))

def sieve2(n):
	"""Using unpack operator instead of list cast."""
	
	A = [True] * (n + 1)
	
	for i in range(2, int(sqrt(n)) + 1):
		if A[i]:
			A[i*i::i] = [False] * (((n+1)-i*i-1)//i+1)
	
	return [*compress(range(2, n + 1), A[2:])]

def sieve3(n):
	"""Only checking odd numbers."""
	
	A = [True] * (n + 1)
	
	for i in range(3, int(sqrt(n)) + 1, 2):
		if A[i]:
			A[i*i::i] = [False] * (((n+1)-i*i-1)//i+1)
	
	return [2, *compress(range(3, n + 1, 2), A[3::2])]

def sieve4(n):
	"""Only storing odd numbers."""
	
	A = [True] * ((n + 1) // 2)
	
	for i in range(3, int(sqrt(n)) + 1, 2):
		if A[i // 2]:
			A[i*i//2::i] = [False] * (((n+1)//2-i*i//2-1)//i+1)
	
	return [2, *compress(range(3, n + 1, 2), A[1:])]

def sieve5(n):
	"""Using a bytearray."""
	
	A = bytearray([True]) * ((n + 1) // 2)
	
	for i in range(3, int(sqrt(n)) + 1, 2):
		if A[i // 2]:
			A[i*i//2::i] = bytearray(((n+1)//2-i*i//2-1)//i+1)
	
	return [2, *compress(range(3, n + 1, 2), A[1:])]

def sieve6(n, bytearray=bytearray, range=range, int=int, sqrt=sqrt, compress=compress):
	"""Local variables."""
	
	A = bytearray([True]) * ((n + 1) // 2)
	
	for i in range(3, int(sqrt(n)) + 1, 2):
		if A[i // 2]:
			A[i*i//2::i] = bytearray(((n+1)//2-i*i//2-1)//i+1)
	
	return [2, *compress(range(3, n + 1, 2), A[1:])]


functions = [sieve, sieve2, sieve3, sieve4, sieve5, sieve6]

if __name__ == "__main__":
	for func in functions:
		print(f"{func.__doc__}")
		time = timeit("func(10000000)", number=1, globals=globals())
		print(f"{func.__name__} took {time} seconds.\n")
