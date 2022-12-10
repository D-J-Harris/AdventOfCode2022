import numpy as np
import sys
np.set_printoptions(suppress = True, linewidth = np.nan, threshold = sys.maxsize)

class Machine:
    def __init__(self, instructions) -> None:
        self.instructions = instructions
        self.crt = []
        self.crt_width = 40
        self.crt_height = 6
        self.X = 1
        self.cycle = 0
    
    def process(self):
        [self.__process_instruction(instr) for instr in self.instructions]

    def __process_instruction(self, instruction):
        match instruction.split():
            case ['noop']: 
                self.crt.append(u'\u2588') if self.cycle % self.crt_width in (self.X - 1, self.X, self.X + 1) else self.crt.append(' ')
                self.cycle += 1
            case ['addx', x]: 
                self.crt.append(u'\u2588') if self.cycle % self.crt_width in (self.X - 1, self.X, self.X + 1) else self.crt.append(' ')
                self.crt.append(u'\u2588') if (self.cycle + 1) % self.crt_width in (self.X - 1, self.X, self.X + 1) else self.crt.append(' ')
                self.cycle += 2
                self.X += int(x)




if __name__ == "__main__":
    with open ('inputs/input-10.txt') as f:
        machine = Machine(f.read().split('\n'))
    
    machine.process()
    [print(''.join(x)) for x in np.reshape(machine.crt, (machine.crt_height, machine.crt_width))]
