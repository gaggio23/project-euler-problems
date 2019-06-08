# Goldbach's other conjecture
#
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
#
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from my_modules import primes as p, math as m

LIMIT = 5800

odds = set()
for n in range(9, LIMIT, 2):
    odds.add(n)
primes = p.sieve_of_eratosthenes(LIMIT)
odd_coprimes = list(odds.difference(set(primes)))

for oc in odd_coprimes:
    res = 0
    for p in primes:
        if p > oc:
            break
        elif ((oc - p) / 2) != ((oc - p) // 2):
            continue
        elif m.is_square((oc - p) // 2):
            res = oc
            print(f"{oc} = {p} + 2*{(oc - p) // 2}")
            break
    if res == 0:
        print(f"NUMBER FOUND! : {oc}")
        break
