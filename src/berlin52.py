from util import *
from heuristics import NearestNeighbor, NearestNeighborD

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
nnd = NearestNeighborD()

start_city = cities[0]
# path = nn.path(start_city, cities)
path = nnd.build_path(start_city, cities)

distance = 0
for node in path:
    distance += node[1]

print("Distance:", distance)
