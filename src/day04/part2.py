if __name__ == "__main__":
    result = 0
    with open('inputs/input-04.txt', 'r') as f:
        for pairs in f.read().split('\n'):
            pair_one, pair_two = pairs.split(',')
            low_one, high_one = map(int, pair_one.split('-'))
            low_two, high_two = map(int, pair_two.split('-'))

            if low_two >= low_one and low_two <= high_one:
                result += 1
                continue
            if low_one >= low_two and low_one <= high_two:
                result += 1
                continue

    print(f'answer to puzzle 4, part 2 is {result}')
