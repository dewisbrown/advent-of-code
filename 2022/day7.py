'''The filesystem consists of a tree of files (plain data) 
and directories (which can contain other directories or files). 
The outermost directory is called /. 
You can navigate around the filesystem, 
moving into or out of directories and listing 
the contents of the directory you're currently in.

Within the terminal output, lines that begin with $ are 
commands you executed, very much like some modern computers:


-cd means change directory. This changes which directory is the 
current directory, but the specific result depends on the argument:
    -cd x moves in one level: it looks in the current directory 
    for the directory named x and makes it the current directory.
    -cd .. moves out one level: it finds the directory that 
    contains the current directory, then makes that directory 
    the current directory.
    -cd / switches the current directory to the outermost directory, /.
-ls means list. It prints out all of the files and directories 
immediately contained by the current directory:
    -123 abc means that the current directory 
    contains a file named abc with size 123.
    -dir xyz means that the current directory 
    contains a directory named xyz.
'''

class Node:
    '''Represents directory folder.'''
    parent = None
    children = []
    size = 0

    def __init__(self, name: str, parent):
        self.name = name.strip()
        self.parent = parent


    def __str__(self) -> str:
        return f'{self.name} - ({self.size})'


    def add_child(self, child):
        self.children.append(child)


    def set_size(self, size: int) -> None:
        self.size = size


    def calculate_size(self):
        if len(self.children) > 0:
            for child in self.children:
                self.size += child.size


def parse_line(line: str, parent_node: Node) -> Node:
    if line[:3] == 'dir':
        return Node(name=line[4:].strip(), parent=parent_node)
    else:
        size, name = line.split(' ')
        node = Node(name=name, parent=parent_node)
        node.set_size(size=size)
        return node


# read data from text file
with open('2022/input-text/day7.txt', encoding='utf-8') as file:    # change txt filepath when debug
    data = file.readlines()

# program start
if __name__ == '__main__':
    root = Node('/', parent=None)
    curr: Node = root

    for i in range(1, len(data) - 1):
        # change directory
        if '$ cd' in data[i]:
            target_dir = data[i][5:].strip()
            # go out one level
            if target_dir == '..':
                curr = curr.parent
            # go in one level
            else:
                for child in curr.children:
                    if child.name == target_dir:
                        curr = child
        
        # ls command
        if '$ ls' in data[i]:
            i += 1
            while '$' != data[i][0] and i < len(data) - 1:
                node: Node = parse_line(line=data[i], parent_node=curr)
                curr.add_child(node)
                i += 1
