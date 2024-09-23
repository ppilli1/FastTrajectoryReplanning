from repeatedA import repeated_forward_a_star, repeated_backward_a_star
from adaptiveA import adaptive_a_star
import time

def compare_algorithms(grid, start, goal):
    algorithms = {
        "Repeated Forward A*": repeated_forward_a_star,
        "Repeated Backward A*": repeated_backward_a_star,
        "Adaptive A*": adaptive_a_star
    }

    for name, algo in algorithms.items():
        start_time = time.time()
        path = algo(grid, start, goal)
        end_time = time.time()
        if path:
            print(f"{name} found a path of length {len(path)} in {end_time - start_time:.4f} seconds")
        else:
            print(f"{name} could not find a path")
