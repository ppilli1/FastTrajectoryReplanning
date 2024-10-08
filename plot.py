import numpy as np
import random
import os

grid_size = (6, 6)    
num_grids = 5             
block_probability = 0.3  


def generate(grid_size, block_probability):
    grid = np.full(grid_size, -1)
    visited = set()
    stack = []

    start = (0, 0)
    goal = (grid_size[0] - 1, grid_size[1] - 1)

    grid[start] = 0
    grid[goal] = 0
    visited.add(start)
    stack.append(start)

    while stack:
        current = stack[-1]
        neighbors = []

        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + d[0], current[1] + d[1])
            if (0 <= neighbor[0] < grid_size[0] and 0 <= neighbor[1] < grid_size[1]
                and neighbor not in visited and grid[neighbor] == -1):
                neighbors.append(neighbor)

        if neighbors:
            next_cell = random.choice(neighbors)
            if random.random() < block_probability:
                if next_cell != start and next_cell != goal:
                    grid[next_cell] = 1
            else:
                grid[next_cell] = 0
                stack.append(next_cell)
            visited.add(next_cell)
        else:
            stack.pop()

        if not stack:
            unvisited_cells = np.argwhere(grid == -1)
            if unvisited_cells.size > 0:
                new_start = tuple(unvisited_cells[random.randint(0, len(unvisited_cells) - 1)])
                if new_start != start and new_start != goal:
                    grid[new_start] = 0
                stack.append(new_start)
                visited.add(new_start)

    return grid, visited


def save_gridworlds(num_grids, grid_size, block_probability):
    folder_name = 'gridworlds'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    grids = []
    for i in range(num_grids):
        grid, visited = generate(grid_size, block_probability) 
        print(f'Grid {i} has {len(visited)} visited cells.')
        grids.append(grid)

        
        grid_file_path = os.path.join(folder_name, f'gridworld_{i}.npy')
        np.save(grid_file_path, grid)

    return grids

def main():
    save_gridworlds(num_grids, grid_size, block_probability)

if __name__ == '__main__':
    main()
