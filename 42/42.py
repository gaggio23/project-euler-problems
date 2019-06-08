# Coded triangle numbers

# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are: 
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values 
# we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
# If the word value is a triangle number then we shall call the word a triangle word.
# 
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, 
# how many are triangle words?

from ast import literal_eval
from my_modules import math as m, strings as s


triangle_numbers = m.nth_triangle_numbers(18)
with open("p042_words.txt", 'r') as file:
	words = literal_eval(file.read())
	count = 0
	for word in words:
		if s.word_value(word) in triangle_numbers:
			print(f"{word} : {s.word_value(word)}")
			count += 1
print(count) #162