# Pandigital multiples

# Take the number 192 and multiply it by each of 1, 2, and 3:
# 
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
# 
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, 
# which is the concatenated product of 9 and (1,2,3,4,5).
# 
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer 
# with (1,2, ... , n) where n > 1?

from my_modules import digits as d

answer = 0
for i in range(9999):
	for j in range(2, 10):
		res = ""
		for k in range(1, j):
			res += str(i * k)
		res = int(res)
		if (d.digits_number(res) == 9) and d.is_number_pandigital(res):
			print(i, j - 1, res)
			if res > answer:
				answer = res
print("########### " + str(answer))