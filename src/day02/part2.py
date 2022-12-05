if __name__ == "__main__":
    scores = []
    with open('inputs/input-02.txt', 'r') as f:
        for round in f.read().split('\n'):
            round_score = 0
            them, us = round.split(' ')
            match us:
                case 'X': 
                    match them:
                        case 'A': round_score += 3
                        case 'B': round_score += 1
                        case 'C': round_score += 2
                case 'Y': 
                    round_score += 3
                    match them:
                        case 'A': round_score += 1
                        case 'B': round_score += 2
                        case 'C': round_score += 3
                case 'Z': 
                    round_score += 6
                    match them:
                        case 'A': round_score += 2
                        case 'B': round_score += 3
                        case 'C': round_score += 1
            scores.append(round_score)
    print(f'answer to puzzle 2, part 2 is {sum(scores)}')
