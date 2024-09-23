from heap import BinaryHeap
from repeatedA import heuristic_manhattan, reconstruct_path

def adaptive_a_star(grid, start, goal):
    open_list = BinaryHeap()
    open_list.push(0, start)

    g_values = {start: 0}
    h_values = {start: heuristic_manhattan(start, goal)}
    closed_set = set()

    max_iterations = grid.shape[0] * grid.shape[1] 
    iteration_count = 0

    while not open_list.is_empty() and iteration_count < max_iterations:
        current = open_list.pop()

        if current == goal:
            update_heuristics(h_values, g_values, goal)
            return reconstruct_path(current, g_values, start)

        closed_set.add(current)

        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + d[0], current[1] + d[1])
            if (0 <= neighbor[0] < grid.shape[0] and 
                0 <= neighbor[1] < grid.shape[1] and 
                neighbor not in closed_set and grid[neighbor] == 0):

                tentative_g = g_values[current] + 1
                if neighbor not in g_values or tentative_g < g_values[neighbor]:
                    g_values[neighbor] = tentative_g
                    h_values[neighbor] = heuristic_manhattan(neighbor, goal)
                    f_value = tentative_g + h_values[neighbor]
                    open_list.push(f_value, neighbor)

        iteration_count += 1
    
    print("Exceeded maximum iterations. No path found.")
    return None 


def update_heuristics(h_values, g_values, goal):
    for cell in g_values:
        h_values[cell] = g_values[goal] - g_values[cell]
