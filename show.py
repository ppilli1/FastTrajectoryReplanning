import numpy as np
import matplotlib.pyplot as plt


def visualize_grid(grid):
    plt.imshow(grid, cmap='binary')  
    plt.gca().set_xticks(np.arange(len(grid[0])) - 0.5)
    plt.gca().set_yticks(np.arange(len(grid)) - 0.5)
    plt.grid(True)
    plt.gca().set_xticklabels([])
    plt.gca().set_yticklabels([])
    plt.title('Grid World')
    plt.show()

for i in range(5):
    grid = np.load(f'gridworld_{i}.npy')
    visualize_grid(grid)