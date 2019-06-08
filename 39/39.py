# Integer right triangles

# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# 
# For which value of p ≤ 1000, is the number of solutions maximised?

from my_modules import math as m

max_triples = 0
for sides_sum in range(0, 1001, 60):
	triples = m.get_pythagorian_triples(sides_sum)
	if len(triples) > max_triples:
		max_triples = len(triples)
		print(f"For perimeter {sides_sum} triples are {len(triples)}: {triples}")
print("#####" + str(max_triples))