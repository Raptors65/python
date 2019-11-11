from functools import reduce
from math import sqrt

def product(*nums):
	"""Returns the product of any amount of integers."""
	return reduce((lambda x, y: x * y), nums)


def gcd_for_two(a, b):
	"""Returns the GCD of two integers.
	
	Uses the Euclidean algorithm. Based on pseudocode from Wikipedia.
	"""
	
	while b != 0:
		temp = b
		b = a % b
		a = temp
	return a


def gcd(*nums):
	"""Returns the GCD of any amount of integers.
	
	Uses the Euclidean algorithm along with iteration.
	"""
	
	return reduce(gcd_for_two, nums)


def lcm_for_two(a, b):
	"""Returns the LCM of two integers.
	
	Uses the GCD function as a / gcd(a, b) * b.
	"""
	
	return a // gcd_for_two(a, b) * b


def lcm(*nums):
	"""Returns the LCM of any amount of integers.
	
	Uses lcm_for_two along with iteration.
	"""
	
	return reduce(lcm_for_two, nums)

def prime_factorization(n):
	"""Returns the prime factorization of an integer as a list."""
	
	primes = []
	
	while not n % 2:
		primes.append(2)
		n //= 2
	
	for possible_factor in range(3, int(sqrt(n)) + 1, 2):
		while not n % possible_factor:
			primes.append(i)
			n //= possible_factor
	
	if n > 1:
		primes.append(n)
	return primes

def is_prime(n):
	"""Checks if an integer is prime."""
	
	if n < 2:
		return False
	
	if not n % 2:
		return False
	
	for possible_factor in range(3, int(sqrt(n)) + 1, 2):
		if not n % possible_factor:
			return False
	return True
	
	

for func in [product, gcd_for_two, gcd, lcm_for_two, lcm, prime_factorization, is_prime]:
	print(func.__name__ + "\n" + func.__doc__ + "\n")
