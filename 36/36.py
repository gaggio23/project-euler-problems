# Double-base palindromes

# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# 
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# 
# (Please note that the palindromic number, in either base, may not include leading zeros.)

from my_modules import strings as s
from my_modules import math as m

res = 0
for n in range(1, 1000000, 2):
	if s.is_palindrome(str(n)) and s.is_palindrome(m.base_conversion(n, 2)):
		res += n
print(res)