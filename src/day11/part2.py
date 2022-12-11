global divisor
divisor = 1
class Monkey:
    def __init__(self, items, operation, test, true_target, false_target) -> None:
        self.items = items
        self.operate = lambda old : eval(operation)
        self.test = test
        self.true_target = true_target
        self.false_target = false_target
        self.inspect_count = 0
    
    # defines which monkey an inspected item will be thrown to, followed by its worry level
    def inspect(self, item):
        self.inspect_count += 1
        worry_level = self.operate(item)
        worry_level = worry_level % divisor
        return (self.false_target if (worry_level % self.test) else self.true_target, worry_level)

if __name__ == "__main__":
    monkeys: list[Monkey] = []
    f = open ('inputs/input-11.txt')
    for monkey_text in f.read().split('\n\n'):
        for instr in monkey_text.split('\n'):
            match instr.split():
                case ["Starting", "items:", *items]: items = map(lambda x: x.replace(',', ''), items)
                case ["Operation:", "new", "=", *operation]: operation = ' '.join(operation)
                case ["Test:", "divisible", "by", test]: divisor *= int(test)
                case ["If", "true:", "throw", "to", "monkey", true_target]: pass
                case ["If", "false:", "throw", "to", "monkey", false_target]: pass
        monkeys.append(Monkey(list(map(int, items)), operation, int(test), int(true_target), int(false_target)))
    f.close()

    for _ in range(10000):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.items.pop()
                target, item = monkey.inspect(item)
                monkeys[target].items.append(item)
    
    sorted_inspections = sorted(list(map(lambda x: x.inspect_count, monkeys)))
    print(f'answer to puzzle 11, part 2 is {sorted_inspections[-1] * sorted_inspections[-2]}')
