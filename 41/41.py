# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
# For example, 2143 is a 4-digit pandigital and is also prime.
# 
# What is the largest n-digit pandigital prime that exists?


from my_modules import primes as p, digits as d


for n in range(9999999, 1, -2):
	if d.is_number_pandigital(n) and p.is_prime(n):
		print(n)