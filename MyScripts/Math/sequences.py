import itertools
import math

def primes():
	# Looping through possible prime numbers.
	for n in itertools.count(2):
		# Looping through possible factors.
		for i in range(2, int(math.sqrt(n)) + 1):
			# Checking if i is a factor of n.
			if n % i == 0:
				# Leaving the loop.
				break
		else:
			# If break wasn't called, n must be prime.
			yield n

def fibonacci():
	# First two Fibonacci numbers.
	a = 1
	b = 1
	# Yielding the first two Fibonacci numbers.
	yield 1
	yield 1
	# Looping forever.
	while True:
		# Saving b in a and the sum of a and b in b.
		a, b = b, a + b
		# Yielding the new Fibonacci number.
		yield b

