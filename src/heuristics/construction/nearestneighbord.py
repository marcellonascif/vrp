from collections import deque
from util import *
from .nearestneighbor import NearestNeighbor

class NearestNeighborD:

    def find_nearest_neighbor(self, left_node: Node, right_node: Node, nodes: list):
        '''
        Heuristic function to find the nearest neighbor of a given node
        '''

        left_nearest_node = left_node
        right_nearest_node = right_node

        left_nearest_distance = float('inf')
        right_nearest_distance = float('inf')


        for node in nodes:
            left_distance = euc_distance(left_node, node)
            right_distance = euc_distance(right_node, node)

            if left_distance < left_nearest_distance:
                left_nearest_node = node
                left_nearest_distance = left_distance

            if right_distance < right_nearest_distance:
                right_nearest_node = node
                right_nearest_distance = right_distance

        if left_nearest_distance <= right_nearest_distance:
            return left_nearest_node, left_node

        else:
            return right_node, right_nearest_node

    def build_path(self, start_node, unvisited):
        '''
        Find the path through the nearest neighbors
        '''

        nn = NearestNeighbor()
        path = deque()

        left_node = start_node
        unvisited.remove(left_node)

        right_node, right_distance = nn.find_nearest_neighbor(left_node, unvisited)
        unvisited.remove(right_node)

        path.append([left_node, right_node])

        while unvisited:
            full_left_node = left_node
            full_right_node = right_node

            left_node, right_node = self.find_nearest_neighbor(left_node, right_node, unvisited)

            if left_node in unvisited:
                unvisited.remove(left_node)
                path.appendleft([left_node, right_node])

                right_node = full_right_node

            elif right_node in unvisited:
                unvisited.remove(right_node)
                path.append([left_node, right_node])

                left_node = full_left_node

        # add the distance from the last node to the first node in the first element of the path
        path.append([path[-1][1], path[0][0]])

        return path
