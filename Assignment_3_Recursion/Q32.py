class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def print_leaf_nodes(root):
 
    if not root:
        return
    
   
    if not root.left and not root.right:
        print(root.value, end=" ")
    
    
    print_leaf_nodes(root.left)
    print_leaf_nodes(root.right)

root = TreeNode(4,TreeNode(2, TreeNode(1), TreeNode(3)),TreeNode(6, TreeNode(5), TreeNode(7)))
print("Leaf nodes of BST:")
print_leaf_nodes(root)
print() 
