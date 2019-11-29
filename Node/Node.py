

class Node:
    def __init__(self, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right


node1 = Node()
node2 = Node('one','two', 'three')



print(""another test)
print(node1.left)
print(node1.right)
print(node1.parent)
print()
print(node2.left)
print(node2.right)
print(node2.parent)
