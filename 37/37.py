# Truncatable primes

# The number 3797 has an interesting property. Being prime itself, it is possible to continuously 
# remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
# Similarly we can work from right to left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# 
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from my_modules import primes as p



primes = p.sieve_of_eratosthenes(1000000)
res = 0
for prime in primes[4:]:
	if p.is_lr_prime(prime) and p.is_rl_prime(prime):
		print(prime)
		res += prime
print("##Result is: " + str(res))