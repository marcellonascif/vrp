from util import *

def calculate_total_distance(path):
    total_distance = sum(node[1] for node in path)
    return total_distance

class TwoOpt:

    def optimize_path(path):
        best_path = path[:]
        best_distance = calculate_total_distance(best_path)
        improved = True

        while improved:
            improved = False
            for i in range(1, len(best_path) - 2):
                for j in range(i + 1, len(best_path)):
                    # Gerar uma nova rota invertendo os nós entre i e j
                    new_path = best_path[:i] + best_path[i:j][::-1] + best_path[j:]
                    new_distance = calculate_total_distance(new_path)

                    if new_distance < best_distance:
                        best_distance = new_distance
                        best_path = new_path
                        improved = True
            if improved:
                print(f"Melhoria encontrada: {best_distance}")

        return best_path, best_distance
