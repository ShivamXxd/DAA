class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_leaf_nodes(root):
    if root:
        if root.left is None and root.right is None:
            print(root.val, end=" ")
        print_leaf_nodes(root.left)
        print_leaf_nodes(root.right)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

print("Leaf nodes of the Binary Search Tree:")
print_leaf_nodes(root)
