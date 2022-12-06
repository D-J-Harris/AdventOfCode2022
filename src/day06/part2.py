from collections import defaultdict

tracker = defaultdict(int)
if __name__ == "__main__":
    marker = 14
    with open('inputs/input-06.txt', 'r') as f:
        seq = f.read().strip()
    for letter in seq[:marker]: tracker[letter] += 1
    
    for num, letter in enumerate(seq[marker:]):
        tracker[letter] +=1
        if tracker[seq[num]] == 1:
            del tracker[seq[num]]
        else: tracker[seq[num]] -= 1

        if len(tracker) == marker: 
            print(f'answer to puzzle 6, part 2 is {num + marker + 1}')
            break
