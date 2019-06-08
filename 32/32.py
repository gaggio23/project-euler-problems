# Pandigital Products:
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# 
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product 
# is 1 through 9 pandigital.
# 
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# 
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

from my_modules import search as s, digits as d


diff_digits_nums = []
for n in range(2, 10000):
	if d.has_different_digits(n):
		diff_digits_nums.append(n)
products_to_sum = set()
for i in diff_digits_nums[::-1]:
	for j in diff_digits_nums[:s.binary_search(diff_digits_nums, i//2, False) + 1]:
		if i % j == 0 and d.has_different_digits(i//j):
			candidate = d.join_numbers(j, i//j, i)
			if d.number_of_digits(candidate) == 9 and d.is_number_pandigital(candidate):
				products_to_sum.add(i)
				print(f"{j} * {i//j} = {i}")
print(products_to_sum)
print(sum(products_to_sum))