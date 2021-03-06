"""
Knapsack Problem Dynamic Programming Algorithm

Max capacity: k
I: set of all items
w_i: weight of item i
v_i: value of item i

Sort values by values density: v_i/w_i
"""
import numpy as np
#Item = namedtuple("Item", ['index', 'value', 'weight', 'density'])

def dynamic(item_count, capacity, items):
	# items.sort(key=lambda x:x.density, reverse=True)

	table = np.zeros((capacity + 1, item_count + 1))

	for col in range(1, item_count + 1):
		val = items[col-1].value
		wht = items[col-1].weight
		for row in range(1, capacity + 1):
			if row<wht:
				table[row][col]=table[row][col-1]
			else:
				table[row][col]=max(val+table[row-wht][col-1], table[row][col-1])

	sum = table[capacity][item_count]

	row = capacity
	col = item_count
	val = table[row][col]

	value = val
	weight = -1
	taken = [0]*item_count

	while col>0:
		if table[row][col]!=table[row][col-1]:
			taken[col-1]=1
			row -= items[col-1].weight
			col -= 1
		else:
			col -= 1

	return int(value), weight, taken



