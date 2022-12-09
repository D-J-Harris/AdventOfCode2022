def follow_head(head, tail):
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]
    if x_diff > 1 or (x_diff > 0 and y_diff not in (-1, 0, 1)): tail[0] += 1
    if x_diff < -1 or (x_diff < 0 and y_diff not in (-1, 0, 1)): tail[0] -= 1
    if y_diff > 1 or (y_diff > 0 and x_diff not in (-1, 0, 1)): tail[1] += 1
    if y_diff < -1 or (y_diff < 0 and x_diff not in (-1, 0, 1)): tail[1] -= 1
    return tail

if __name__ == "__main__":
    with open ('inputs/input-09.txt') as f:
        tail_set = set()
        head, tail = [0, 0], [0, 0]
        for instr in f.read().split('\n'):
            dir, steps = instr.split(' ')
            steps = int(steps)
            for _ in range(steps):
                match dir:
                    case 'U': head[1] += 1
                    case 'D': head[1] -= 1
                    case 'L': head[0] -= 1
                    case 'R': head[0] += 1
                tail = follow_head(head, tail)
                tail_set.add(tuple(tail))
    print(f'answer to puzzle 9, part 1 is {len(tail_set)}')
