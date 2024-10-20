from util import *

class NearestNeighbor:

    def find_nearest_neighbor(self, start_node: Node, nodes: list):
        '''
        Heuristic function to find the nearest neighbor of a given node

        :return:\n
                - Node: The nearest neighbor\n
                - float: The distance to the nearest neighbor\n
                - List: The remaining nodes
        :rtype: The nearest neighbor, the distance to the nearest neighbor, and the remaining nodes
        '''

        nearest_node = start_node
        nearest_distance = float('inf')

        for node in nodes:
            distance = euc_distance(start_node, node)

            if distance < nearest_distance:
                nearest_node = node
                nearest_distance = distance

        return nearest_node

    def build_path(self, start_node, unvisited):
        '''
        Find the path through the nearest neighbors
        '''

        path = []

        node = start_node
        unvisited.remove(node)

        while unvisited:
            old_node = node
            node = self.find_nearest_neighbor(old_node, unvisited)

            unvisited.remove(node)
            path.append([old_node, node])

        # add the distance from the last node to the first node in the first element of the path
        path.append([path[-1][1], path[0][0]])

        return path
