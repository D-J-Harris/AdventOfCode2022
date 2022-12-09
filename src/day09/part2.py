def follow_knot(leader, follower):
    x_diff = leader[0] - follower[0]
    y_diff = leader[1] - follower[1]
    if x_diff > 1 or (x_diff > 0 and y_diff not in (-1, 0, 1)): follower[0] += 1
    if x_diff < -1 or (x_diff < 0 and y_diff not in (-1, 0, 1)): follower[0] -= 1
    if y_diff > 1 or (y_diff > 0 and x_diff not in (-1, 0, 1)): follower[1] += 1
    if y_diff < -1 or (y_diff < 0 and x_diff not in (-1, 0, 1)): follower[1] -= 1
    return follower

if __name__ == "__main__":
    with open ('inputs/input-09.txt') as f:
        tail_set = set()
        num_knots = 10
        knots = [[0, 0] for _ in range(num_knots)]
        for instr in f.read().split('\n'):
            dir, steps = instr.split(' ')
            steps = int(steps)
            for _ in range(steps):
                match dir:
                    case 'U': knots[0][1] += 1
                    case 'D': knots[0][1] -= 1
                    case 'L': knots[0][0] -= 1
                    case 'R': knots[0][0] += 1
                for leader_position in range(num_knots - 1):
                    follower = follow_knot(knots[leader_position], knots[leader_position + 1])
                    knots[leader_position + 1] = follower
                tail_set.add(tuple(knots[-1]))
    print(f'answer to puzzle 9, part 2 is {len(tail_set)}')
