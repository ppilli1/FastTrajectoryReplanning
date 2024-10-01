from test import compare_algorithms
import numpy as np
from plot import save_gridworlds
import os
import matplotlib.pyplot as plt
num_grids = 5
grid_size = (101, 101)
block_probability = 0.3   

def is_unreachable(grid, start, goal):
    
    rows, cols = grid.shape

    
    goal_x, goal_y = goal
    start_x, start_y = start

    
    if grid[start] == 1 or grid[goal] == 1:
        print(f"Start or goal is blocked.")
        return True

    
    if goal_x > 0 and goal_y > 0: 
        if grid[goal_x - 1, goal_y] == 1 and grid[goal_x, goal_y - 1] == 1:
            print("Goal is unreachable: goal is blocked from above and left.")
            return True

    
    if start_x < rows - 1 and start_y < cols - 1: 
        if grid[start_x + 1, start_y] == 1 and grid[start_x, start_y + 1] == 1:
            print("Goal is unreachable: start is blocked to the right and below.")
            return True

    return False

def visualize_grid(grid):
    plt.imshow(grid, cmap='binary')  
    plt.gca().set_xticks(np.arange(len(grid[0])) - 0.5)
    plt.gca().set_yticks(np.arange(len(grid)) - 0.5)
    plt.grid(True)
    plt.gca().set_xticklabels([])
    plt.gca().set_yticklabels([])
    plt.title('Grid World')
    plt.show()  
        
def main():
    folder_name = 'gridworlds'
    save_gridworlds(num_grids, grid_size, block_probability)

    for i in range(num_grids):
        grid_file_path = os.path.join(folder_name, f'gridworld_{i}.npy')
        grid = np.load(grid_file_path)
        visualize_grid(grid)
        start = (0, 0)
        goal = (grid_size[0] - 1, grid_size[1] - 1)

        
        if is_unreachable(grid, start, goal):
            print(f"Grid {i}: Start or goal is unreachable. Skipping.")
            continue

        
        compare_algorithms(grid, start, goal)


    
if __name__ == '__main__':
    main()
