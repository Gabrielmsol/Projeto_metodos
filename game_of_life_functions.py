import numpy as np


def create_grid(rows_cols, P):
    return np.random.choice([0, 1], size=(rows_cols, rows_cols), p=[1-P, P])


# Updates the grid following Conway's game of life rules
def update_grid(grid):
    neighbours = np.zeros_like(grid)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            neighbours += np.roll(np.roll(grid, i, axis=0), j, axis=1)
            # Smart trick to count neighbours we roll the grid summing values over a point

    new_grid = np.where((grid == 1) & ((neighbours < 2) | (neighbours > 3)), 0, grid)
    new_grid = np.where((grid == 0) & (neighbours == 3), 1, new_grid)
    # This makes, so we update our grid according to Conway's law
    return new_grid
  
