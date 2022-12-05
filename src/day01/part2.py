if __name__ == "__main__":
    results = []
    with open('inputs/input-01.txt', 'r') as f:
        for elf_num, calorie_list in enumerate(f.read().split('\n\n')):
            calorie_list = calorie_list.split('\n')
            results.append(sum(map(int, calorie_list)))
    results.sort()
    print(f'answer to puzzle 1, part 2 is {sum(results[-3:])}')
