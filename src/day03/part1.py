if __name__ == "__main__":
    letterToNum = lambda letter : ord(letter) - 96 if letter.islower() else ord(letter) - 38
    results = []
    with open('inputs/input-03.txt', 'r') as f:
        for items in f.read().split('\n'):
            half = len(items) // 2
            first, second = items[:half], items[half:]

            intersect = set(first) & set(second)
            results.append(letterToNum(intersect.pop()))
    print(f'answer to puzzle 3, part 1 is {sum(results)}')
