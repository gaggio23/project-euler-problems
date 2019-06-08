# Distinct primes factors
#
# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?


from my_modules import primes as p

LIMIT = 200000

primes = p.sieve_of_eratosthenes(LIMIT)
counter = 0
for i in range(645, LIMIT):
    fact = p.prime_factorization(i, primes)
    if len(fact) == 4:
        counter += 1
        if counter == 4:
            print(f"DONE! number is {i - 3}")
            break
    else:
        counter = 0