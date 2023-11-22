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
class Tree:
    '''Tree structure.'''
    def __init__(self, node):
        self.root = node
        self.directory = node


    def set_dir(self, node):
        self.directory = node


    def get_dir(self):
        return self.directory


    def __str__(self):
        res = self.root.name
        for child in self.root.children:
            res += f'\n\t{child}'
        return res


class DirNode:
    '''Represents directory node.'''
    def __init__(self, name: str):
        self.name = name.strip()
        self.children = []
        self.size = 0

        if name != '/':
            self.parent = tree.get_dir()


    def add_child(self, node):
        self.children.append(node)


    def get_parent(self):
        return self.parent


    def __str__(self) -> str:
        return f'dir {self.name} - [{self.size}]'


class FileNode:
    '''Represents file node.'''
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


    def __str__(self):
        return f'file {self.name} - [{self.size}]'


def parse_line(line: str):
    if line[:3] == 'dir':
        tree.get_dir().add_child(DirNode(name=line[4:].strip()))
    else:
        size, name = line.split(' ')
        tree.get_dir().add_child(FileNode(name=name.strip(), size=int(size)))


# read data from text file
with open('input-text/day7.txt', encoding='utf-8') as file:    # change txt filepath when debug
    data = file.readlines()

# program start
if __name__ == '__main__':
    tree = Tree(DirNode('/'))

    for i in range(1, len(data) - 1):
        # change directory
        if '$ cd' in data[i]:
            target_dir = data[i][5:].strip()
            # go out one level
            if target_dir == '..':
                tree.set_dir(tree.get_dir().get_parent())
            # go in one level
            else:
                for child in tree.get_dir().children:
                    if child.name == target_dir:
                        tree.set_dir(child)

        # ls command
        if '$ ls' in data[i]:
            i += 1
            while '$' != data[i][0] and i < len(data) - 1:
                if data[i][:3] == 'dir':
                    tree.get_dir().add_child(DirNode(name=data[i][4:].strip()))
                else:
                    size, name = data[i].split(' ')
                    tree.get_dir().add_child(FileNode(name=name.strip(), size=int(size)))
                i += 1
