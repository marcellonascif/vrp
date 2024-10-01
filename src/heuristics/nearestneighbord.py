from collections import deque
from util import *
from heuristics.nearestneighbor import NearestNeighbor

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

        print("left node: ", left_node, "| right node", right_node)
        if left_nearest_distance <= right_nearest_distance:
            print("left nearest node: ", left_nearest_node, "|", left_nearest_distance, "<=", right_nearest_distance, "right nearest node", right_nearest_node)
            return left_nearest_node, right_node, left_nearest_distance, right_nearest_distance

        else:
            print("right nearest node: ", right_nearest_node, "|", right_nearest_distance, "<", left_nearest_distance, "left nearest node", left_nearest_node)
            return left_node, right_nearest_node, left_nearest_distance, right_nearest_distance

    def build_path(self, start_node, unvisited):
        '''
        Find the path through the nearest neighbors
        '''

        nn = NearestNeighbor()
        path = deque()

        left_node, left_distance = start_node, 0
        unvisited.remove(left_node)

        right_node, right_distance = nn.find_nearest_neighbor(left_node, unvisited)
        unvisited.remove(right_node)

        print("start left node: ", left_node, "|", left_distance)
        print("start right node: ", right_node, "|", right_distance)

        path.append([left_node, left_distance])
        path.append([right_node, right_distance])

        while unvisited:
            left_node, right_node, left_distance, right_distance = self.find_nearest_neighbor(left_node, right_node, unvisited)


            if left_node in unvisited:
                unvisited.remove(left_node)
                path[0][1] = left_distance
                path.appendleft([left_node, 0])

            elif right_node in unvisited:
                unvisited.remove(right_node)
                path.append([right_node, right_distance])

            else:
                print("neither in unvisited")

        return path
