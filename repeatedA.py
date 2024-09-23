from heap import BinaryHeap

def repeated_a_star(grid, start, goal, heuristic):
    open_list = BinaryHeap()
    open_list.push(0, start)

    g_values = {start: 0}
    closed_set = set()

    max_iterations = grid.shape[0] * grid.shape[1]
    iteration_count = 0

    while not open_list.is_empty() and iteration_count < max_iterations:
        current = open_list.pop()

        if current == goal:
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
                    f_value = tentative_g + heuristic(neighbor, goal)
                    open_list.push(f_value, neighbor)

        iteration_count += 1
    
    print("Exceeded maximum iterations. No path found.")
    return None 


def heuristic_manhattan(cell, goal):
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

def reconstruct_path(current, g_values, start):
    path = [current]
    
    while current != start:
        valid_neighbors = [(current[0] + d[0], current[1] + d[1]) for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
        
        
        current = min(valid_neighbors, key=lambda c: g_values.get(c, float('inf')))
        
        
        if g_values.get(current, float('inf')) == float('inf'):
            print("Error in reconstructing path: no valid path.")
            break
        
        path.append(current)
    
    return path[::-1]


def repeated_forward_a_star(grid, start, goal):
    return repeated_a_star(grid, start, goal, heuristic_manhattan)


def repeated_backward_a_star(grid, start, goal):
    return repeated_a_star(grid, goal, start, heuristic_manhattan)  


