from util import *

class NearestNeighbor:

    def heuristic(self, start_node: Node, nodes: list):
        '''
        Heuristic function to find the nearest neighbor of a given node

        :return:\n
                - Node: The nearest neighbor\n
                - float: The distance to the nearest neighbor\n
                - list: The remaining nodes
        :rtype: The nearest neighbor, the distance to the nearest neighbor, and the remaining nodes
        '''

        nodes.remove(start_node)
        next_node = start_node
        next_distance = float('inf')

        for node in nodes:
            distance = euc_distance(start_node, node)

            if distance < next_distance:
                next_node = node
                next_distance = distance

        return next_node, next_distance, nodes

    def path(self, nodes):
        '''
        Find the path through the nearest neighbors
        '''

        node = nodes[0]
        distance = 0

        path = []
        path.append([node, distance])

        while nodes:
            node, distance, nodes = self.heuristic(node, nodes)

            if not nodes:
                break

            path.append([node, distance])

        # add the distance from the last node to the first node in the first element of the path
        path[0][1] = euc_distance(path[-1][0], path[0][0])

        return path
