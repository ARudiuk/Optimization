"""
Knapsack Problem Dynamic Programming Algorithm

Max capacity: k
I: set of all items
w_i: weight of item i
v_i: value of item i

Sort values by values density: v_i/w_i
"""
import numpy as np
import pdb
# Item = namedtuple("Item", ['index', 'value', 'weight', 'density'])

"""
Class to act as nodes of tree for branch and bound algorithm
variables:
    parent: node before this one
    value: total value of node
    weight: total weight of node
    depth: how far down the tree, starting at 0
    taken: whether this node includes the item of this depth
fxns:
    get_children:
        generates the children nodes of this node.
        One child will involve excluding an item, and the other
        child will involve including an item 
    get_parent:
        return parent of this node

"""
test_vals = []

class Node:
    def __init__(self, parent, value, weight, depth, taken, idx):
        self.parent = parent
        if parent is not None:
            self.value = parent.value + value * taken
            self.weight = parent.weight + weight * taken
        else:
            self.value = value * taken
            self.weight = weight * taken
        self.depth = depth
        self.taken = taken
        self.idx = idx

    def get_children(self, items):
        a = Node(self, items[self.depth + 1][1], items[self.depth + 1][2], self.depth + 1, 1, items[self.depth+1][0])
        b = Node(self, items[self.depth + 1][1], items[self.depth + 1][2], self.depth + 1, 0, items[self.depth+1][0])
        return a, b

    def get_parent(self):
        return self.parent

def calculate_max(items, capacity, value, weight):
    estimate = value
    current_weight = weight
    for i in range(len(items)):
        if current_weight + items[i][2] < capacity:
            estimate += items[i][1]
            current_weight += items[i][2]
        else:
            estimate += int(items[i][1] * ((capacity-current_weight) / items[i][2]))
            current_weight = capacity
        if current_weight >= capacity:
            return estimate
    return estimate


def bb(item_count, capacity, items):

    to_analyze = []
    items.sort(key=lambda x : x.density, reverse=True)
    a = Node(None, items[0][1], items[0][2], 0, 1, items[0][0])
    a.estimate = calculate_max(items, capacity, 0, 0)
    b = Node(None, 0, 0, 0, 0, items[0][0])
    b.estimate = calculate_max(items[1:], capacity, 0, 0)
    to_analyze.append(b)
    to_analyze.append(a)

    best_node = Node(None, 0, 0, 0, 0, 0)
    # count = 0
    while to_analyze:
        _item = to_analyze.pop()
        if _item.estimate < best_node.value:
            continue
        if _item.weight > capacity:
            continue
        # count += 1
        if _item.depth<item_count-1:
            _item_child_a, _item_child_b = _item.get_children(items)
            _item_child_b.estimate = calculate_max(items[_item.depth+2:], capacity, _item.value, _item.weight)
            _item_child_a.estimate = _item.estimate
            to_analyze.append(_item_child_b)
            to_analyze.append(_item_child_a)
        if _item.depth == item_count - 1:
            if _item.value > best_node.value:
                best_node = _item

    taken = [0]*item_count
    _temp = best_node
    for i in range(_temp.depth+1):
        if _temp.taken == 1:
            taken[_temp.idx] = 1
        _temp = _temp.parent


    # print(count)

    return int(best_node.value), best_node.weight, taken
