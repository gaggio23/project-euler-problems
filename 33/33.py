# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it 
# may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# 
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# 
# There are exactly four non-trivial examples of this type of fraction, less than one in value, 
# and containing two digits in the numerator and denominator.
# 
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

from my_modules import digits as d

for n2 in range(10, 100):
	for d2 in range(n2+1, 100):
		for n1 in range(1, 10):
			for d1 in range(n1+1, 10):
				if n2/d2 == n1/d1 and (n2 % 10 != 0 or d2 % 10 != 0) and d.missing_digit(n2, n1) == d.missing_digit(d2, d1) and d.missing_digit(n2, n1) != None:
					print(f"{n2}/{d2} == {n1}/{d1}")