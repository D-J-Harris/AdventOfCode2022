from collections import defaultdict
import re

if __name__ == "__main__":
    stacks = defaultdict(list)
    with open('inputs/input-05.txt', 'r') as f:
        state, instrs = f.read().split('\n\n')
        for line in state.split('\n')[::-1]:
            line = [line[i : i + 4] for i in range(0, len(line), 4)]
            for stack_num, item in enumerate(line):
                if item.startswith('['): stacks[stack_num + 1].append(item[1])

    for instr in instrs.split('\n'):
        commands = list(map(int, re.findall(r'\d+', instr)))
        tmp = [stacks[commands[1]].pop() for _ in range(int(commands[0]))]
        while tmp: 
            stacks[commands[2]].append(tmp.pop())
    
    print(f'answer to puzzle 5, part 2 is {"".join([x.pop() for x in stacks.values()])}')
