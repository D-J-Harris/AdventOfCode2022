if __name__ == "__main__":
    result = 0
    with open('inputs/input-01.txt', 'r') as f:
        for elf_num, calorie_list in enumerate(f.read().split('\n\n')):
            calorie_list = calorie_list.split('\n')
            result = max(result, sum(map(int, calorie_list)))
    print(f'answer to puzzle 1, part 1 is {result}')
