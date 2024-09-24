from util import *
from heuristics.nearestneighbor import NearestNeighbor

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

        nodes.append(Node(int(node), float(x), float(y)))

    return nodes


cities = read_tsp('data/berlin52.tsp')
# print(cities)

nn = NearestNeighbor()

# nn.heuristic(cities[2], cities)

path = nn.path(cities)
for node in path:
    print(node)
