def calculate_total_distance(path, distance_function):
    for edge in path:
        total_distance += distance_function(edge[0], edge[1])

    return total_distance

def euc_distance(node1, node2):
    return ((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2) ** 0.5
