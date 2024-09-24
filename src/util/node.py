class Node:
    def __init__(self, node: int, x: float, y: float):
        self.node = node
        self.x = x
        self.y = y

    def __repr__(self):
        return f"node {self.node} ({self.x}, {self.y})"
