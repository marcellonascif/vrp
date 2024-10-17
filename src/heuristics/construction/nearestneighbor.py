from util import *

class NearestNeighbor:

    def find_nearest_neighbor(self, start_node: Node, nodes: list):
        '''
        Heuristic function to find the nearest neighbor of a given node

        :return:\n
                - Node: The nearest neighbor\n
                - float: The distance to the nearest neighbor\n
                - list: The remaining nodes
        :rtype: The nearest neighbor, the distance to the nearest neighbor, and the remaining nodes
        '''

        nearest_node = start_node
        nearest_distance = float('inf')

        for node in nodes:
            distance = euc_distance(start_node, node)

            if distance < nearest_distance:
                nearest_node = node
                nearest_distance = distance

        return nearest_node, nearest_distance

    def build_path(self, start_node, unvisited):
        '''
        Find the path through the nearest neighbors
        '''

        path = []

        node, distance = start_node, 0
        unvisited.remove(node)

        path.append([node, distance])

        while unvisited:
            node, distance = self.find_nearest_neighbor(node, unvisited)

            unvisited.remove(node)
            path.append([node, distance])

        # add the distance from the last node to the first node in the first element of the path
        path[0][1] = euc_distance(path[-1][0], path[0][0])

        return path
