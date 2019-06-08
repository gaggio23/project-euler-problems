# Circular primes

# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# 
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# 
# How many circular primes are there below one million?

from my_modules import primes as p

primes = p.sieve_of_eratosthenes(1000000)
count = 0
for prime in primes:
	if p.is_circular_prime(prime):
		count += 1
		print(f"{count} : {prime}")