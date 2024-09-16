class Node:
    def __init__(self, node, x, y):
        self.node = node
        self.x = x
        self.y = y

    def __repr__(self):
        return f"node{self.node} ({self.x}, {self.y})"

def euc_distance(node1, node2):
    return ((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2) ** 0.5
