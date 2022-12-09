import numpy as np

if __name__ == "__main__":
    with open ('inputs/input-08.txt') as f:
        grid = np.stack([np.array(list(x),dtype=int) for x in f.read().split('\n')])
        tracker = np.zeros_like(grid)
        tracker[0,:] = tracker[:,0] = tracker[:,-1] =  tracker[-1,:] = 1
    
    def scan(grid, tracker):
        for row_num, row in enumerate(grid):
            tallest = row[0]
            for col_num, value in enumerate(row):
                if value > tallest:
                    tallest = value
                    tracker[row_num][col_num] = 1
        return tracker
    
    tracker = scan(grid, tracker)
    tracker = scan(grid.T, tracker.T).T
    tracker = np.fliplr(scan(np.fliplr(grid), np.fliplr(tracker)))
    tracker = np.fliplr(scan(np.fliplr(grid.T), np.fliplr(tracker.T))).T
    print(f'answer to puzzle 8, part 1 is {np.sum(tracker)}')
