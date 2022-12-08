from collections import defaultdict

class Tree:
    def __init__(self, _parent: 'Tree' = None):
        self.parent = _parent
        self.children = defaultdict(Tree)
        self.size = 0

    def set_size(self, _size):
        self.size = self.size + _size
        if self.parent: self.parent.set_size(_size)

if __name__ == "__main__":
    root = Tree()
    curr = root
    with open('inputs/input-07.txt', 'r') as f:

        for instr in f.read().split('\n'):
            instr = instr.split(' ')
            match instr[0]:
                case '$':
                    if instr[1] == 'cd':
                        move_to = instr[2]
                        if move_to == '/':
                            curr = root 
                        elif move_to == '..':
                            curr = curr.parent
                        else: curr = curr.children.get(move_to)
                case 'dir':
                    folder_name = instr[1]
                    curr.children[folder_name] = Tree(curr)
                case other:
                    file_size = int(instr[0])
                    file_name = instr[1]
                    child = Tree(curr)
                    child.set_size(file_size)
                    curr.children[file_name] = child
    
    def get_score(node: Tree):
        is_dir = len(node.children) != 0
        return is_dir * (node.size if node.size <= 100000 else 0) + sum([get_score(x) for x in node.children.values()])
    print(f'answer to puzzle 7, part 1 is {get_score(root)}')
