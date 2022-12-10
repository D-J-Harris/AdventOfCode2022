from collections import defaultdict

class Machine:
    def __init__(self, instructions) -> None:
        self.instructions = instructions
        self.cycle_to_X = defaultdict(int)
        self.X = 1
        self.cycle = 1
    
    def process(self):
        [self.__process_instruction(instr) for instr in self.instructions]

    def __process_instruction(self, instruction):
        match instruction.split():
            case ['noop']: 
                self.cycle_to_X[self.cycle] = self.X
                self.cycle += 1
            case ['addx', x]: 
                self.cycle_to_X[self.cycle] = self.X
                self.cycle_to_X[self.cycle + 1] = self.X
                self.cycle += 2
                self.X += int(x)




if __name__ == "__main__":
    with open ('inputs/input-10.txt') as f:
        machine = Machine(f.read().split('\n'))
    
    machine.process()
    target_cycles = [20, 60, 100, 140, 180, 220]
    print(f'answer to puzzle 10, part 1 is {sum([cycle * machine.cycle_to_X[cycle] for cycle in target_cycles])}')
