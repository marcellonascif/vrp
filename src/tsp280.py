from util import *

def read_tsp(file_path):
    with open(file_path) as f:
        lines = f.readlines()

    lines = lines[6:]
    lines = lines[:-2]
    lines = [line.strip() for line in lines]
    lines = [line.split() for line in lines]

    nodes = []
    for line in lines:
        node, x, y = line

        nodes.append(Node(int(node), int(x), int(y)))
        # nodes[int(city)] = {"x": int(x), "y": int(y)}

    return nodes


cities = read_tsp('data/a280.tsp')
print(cities)

print(euc_distance(cities[1], cities[2]))
