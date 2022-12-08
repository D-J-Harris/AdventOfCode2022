import sys
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
    
    unused_space = 70000000 - root.size
    required_space = 30000000 - unused_space
    def get_score(node: Tree):
        is_dir = len(node.children) != 0
        node_score = node.size if is_dir and node.size >= required_space else sys.maxsize
        return min([node_score] + [get_score(x) for x in node.children.values()])
    print(f'answer to puzzle 7, part 2 is {get_score(root)}')
