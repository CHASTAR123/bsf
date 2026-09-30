class Tree:
    def __init__(self, data):
        self.data = data
        self.leftnode = None
        self.rightnode = None

def inordertraversal(root):
    if root.leftnode != None:
        inordertraversal(root.leftnode)
    if root.data % 2 == 0:
        print(root.data)
    if root.rightnode != None:
        inordertraversal(root.rightnode)

root = Tree(6)
root.leftnode = Tree(3)
root.rightnode = Tree(10)
root.leftnode.leftnode = Tree(2)
root.leftnode.rightnode = Tree(5)
root.rightnode.leftnode = Tree(8)
root.rightnode.rightnode = Tree(12)
inordertraversal(root)