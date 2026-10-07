class Tree:
    def __init__(self, data):
        self.data = data
        self.leftnode = None
        self.rightnode = None


def is_bst(node, min_val, max_val):
    if node == None:
        return True
    if node.data < min_val or node.data > max_val:
        return False
    return is_bst(node.leftnode, min_val, node.data) and is_bst(node.rightnode, node.data, max_val)


root = Tree(10)
root.leftnode = Tree(5)
root.rightnode = Tree(15)
root.leftnode.leftnode = Tree(2)
root.leftnode.rightnode = Tree(7)
root.rightnode.leftnode = Tree(12)
root.rightnode.rightnode = Tree(20)

print(is_bst(root, 2, 20))