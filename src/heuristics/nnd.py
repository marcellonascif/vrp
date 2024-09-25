from util import *
from heuristics.nearestneighbor import NearestNeighbor

class NNA:
    def heuristic(self, start_node: Node, nodes: list):
        '''
        Heuristic function to find the nearest neighbor of a given node
        '''

        nn = NearestNeighbor()

        next_node1 = start_node
        next_node2, distance, nodes = nn.heuristic(next_node1, nodes)

        nodes.remove(next_node1)
        nodes.remove(next_node2)

        next_distance1 = float('inf')
        next_distance2 = float('inf')


        for node in nodes:
            distance1 = euc_distance(next_node1, node)
            distance2 = euc_distance(next_node2, node)

            if distance1 < next_distance1:
                next_node1 = node
                next_distance1 = distance1

            if distance2 < next_distance2:
                next_node2 = node
                next_distance2 = distance2

        if next_distance1 < next_distance2:
            return next_node1, next_distance1, nodes
        else:
            return next_node2, next_distance2, nodes
