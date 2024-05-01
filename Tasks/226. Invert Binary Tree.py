# Link:
# https://leetcode.com/problems/invert-binary-tree/


# Code: 
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        # Swap the children
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

def print_tree_by_levels(root):
    from collections import deque
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            print(node.val, end=' ')
            queue.append(node.left)
            queue.append(node.right)
        else:
            print("None", end=' ')
    print()


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Original Tree:")
print_tree_by_levels(root)

solution = Solution()
inverted_root = solution.invertTree(root)

# Inverted Tree
print("Inverted Tree:")
print_tree_by_levels(inverted_root)


# Explanation:
# 1. Base Case: If the current node (root) is None, the function returns None. This check prevents further recursive calls on non-existent children, which is essential for stopping the recursion at the leaf nodes.
# 2. Recursive Swap: The function swaps the left and right children of the current node. It then recursively applies the same logic to the children:
# - It inverts the right subtree and assigns it to root.left.
# - It inverts the left subtree and assigns it to root.right.
# 3. Return: After all descendant nodes are processed and their children are swapped, the current node is returned. This step is crucial as it reconstructs the tree from the bottom up, ensuring that each node is reattached correctly in its new position.
