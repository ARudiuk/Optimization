"""
Knapsack Problem Greedy Algorithm

Max capacity: k
I: set of all items
w_i: weight of item i
v_i: value of item i

Sort values by values density: v_i/w_i
"""
import numpy as np
#Item = namedtuple("Item", ['index', 'value', 'weight', 'density'])

def greedy(item_count, capacity, items):
	items.sort(key=lambda x:x.density, reverse=True)

	value = 0
	weight = 0
	taken = [0]*item_count

	for item in items:
		if weight + item.weight <= capacity:
			taken[item.index] = 1
			value += item.value
			weight += item.weight
	return value, weight, taken



