if __name__ == "__main__":
    scores = []
    with open('inputs/input-02.txt', 'r') as f:
        for round in f.read().split('\n'):
            round_score = 0
            them, us = round.split(' ')
            match us:
                case 'X': 
                    round_score += 1
                    if them == 'A': round_score += 3
                    if them == 'C': round_score += 6
                case 'Y': 
                    round_score += 2
                    if them == 'B': round_score += 3
                    if them == 'A': round_score += 6
                case 'Z': 
                    round_score += 3
                    if them == 'C': round_score += 3
                    if them == 'B': round_score += 6
            scores.append(round_score)
    print(f'answer to puzzle 2, part 1 is {sum(scores)}')
