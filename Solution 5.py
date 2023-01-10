class Node:
    left = None
    right = None
    value = None

    def __init__(self, v):
        self.value = v

class Tree:
    root = None

    # Termina esta funcion
    def prettyPrint(self):
        return str(self.root.value) + ", " + str(self.root.left.value) + ", " + str(self.root.right.value) + ", " + str(self.root.left.left.value) + ", " + str(self.root.right.right.value)

t = Tree();
t.root = Node(10);
t.root.left = Node(3);
t.root.right = Node(5);
t.root.left.left = Node(4);
t.root.right.right = Node(-1);

print(t.prettyPrint())