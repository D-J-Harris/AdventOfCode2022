import numpy as np

if __name__ == "__main__":
    letterToNum = lambda letter : ord(letter) - 96 if letter.islower() else ord(letter) - 38
    groups = []
    with open('inputs/input-03.txt', 'r') as f:
        for items in f.read().split('\n'):
            groups.append(items)
    
    result = 0
    for chunk in np.array_split(groups, len(groups) // 3):
        intersection = set(chunk[0]) & set(chunk[1]) & set(chunk[2])
        result += letterToNum(intersection.pop())
    print(f'answer to puzzle 3, part 2 is {result}')
