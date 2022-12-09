import numpy as np
from itertools import takewhile

if __name__ == "__main__":
    with open ('inputs/input-08.txt') as f:
        grid = np.stack([np.array(list(x),dtype=int) for x in f.read().split('\n')])
        tracker = np.ones_like(grid)
    
    def scan(grid, tracker):
        for row_num, row in enumerate(grid):
            for col_num, value in enumerate(row):
                values_ahead = len(list(takewhile(lambda x: x < value, row[col_num + 1:]))) + 1
                if col_num + values_ahead == len(row): values_ahead -= 1
                tracker[row_num][col_num] *= values_ahead
        return tracker
    
    tracker = scan(grid, tracker)
    tracker = scan(grid.T, tracker.T).T
    tracker = np.fliplr(scan(np.fliplr(grid), np.fliplr(tracker)))
    tracker = np.fliplr(scan(np.fliplr(grid.T), np.fliplr(tracker.T))).T
    print(f'answer to puzzle 8, part 2 is {np.max(tracker)}')
