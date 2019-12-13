import random, time

class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key

def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 
 
def search(root,key): 
      
    # Base Cases: root is null or key is present at root 
    if root is None or root.val == key: 
        return root 
  
    # Key is greater than root's key 
    if root.val < key: 
        return search(root.right,key) 
    
    # Key is smaller than root's key 
    return search(root.left,key) 

def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right) 

def getHeight(node):
    if node == None:
        return -1
    return 1 + max(getHeight(node.left), getHeight(node.right))

treeNum = 1000
height = [None] * treeNum

for i in range(treeNum):
    
    values = random.sample(range(1000000), 100000)
    r = Node(values[0])


    for j in range(0, len(values)):
        insert(r,Node(values[j]))

    height[i] = getHeight(r)

with open('heights.csv', 'w') as f:
    for item in height:
        f.write("%s\n" % item)
