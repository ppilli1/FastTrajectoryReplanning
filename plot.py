import numpy as np
import random

grid_size = (101, 101)    
num_grids = 5             
block_probability = 0.3  

def generate(grid_size, block_probability):
    grid = np.full(grid_size, -1) 
    visited = set()
    stack = []

    start = (random.randint(0, grid_size[0] - 1), random.randint(0, grid_size[1] - 1))
    grid[start] = 0
    visited.add(start)
    stack.append(start)

    while stack:
        current = stack[-1]
        neighbors = []
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
            neighbor = (current[0] + d[0], current[1] + d[1])
            if (0 <= neighbor[0] < grid_size[0] and 
                0 <= neighbor[1] < grid_size[1] and 
                neighbor not in visited and 
                grid[neighbor] == -1):
                neighbors.append(neighbor)

        if neighbors:
            next_cell = random.choice(neighbors)
            if random.random() < block_probability:
                grid[next_cell] = 1 
                visited.add(next_cell)
            else:
                grid[next_cell] = 0 
                visited.add(next_cell)
                stack.append(next_cell)
        else:
            stack.pop()
        if not stack:
            unvisited_cells = np.argwhere(grid == -1)
            if unvisited_cells.size > 0:
                new_start = tuple(unvisited_cells[random.randint(0, len(unvisited_cells) - 1)])
                grid[new_start] = 0
                visited.add(new_start)
                stack.append(new_start)

    return grid,visited

def save_gridworlds(num_grids, grid_size, block_probability):
    grids = []
    for i in range(num_grids):
        grid,visited = generate(grid_size, block_probability)
        print(len(visited))
        grids.append(grid)
        np.save(f'gridworld_{i}.npy', grid)

def main():

    save_gridworlds(num_grids, grid_size, block_probability)
    
if __name__ == '__main__':
    main()


