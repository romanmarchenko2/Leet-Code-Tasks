# Link:
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# Code: 
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Determine the length of the list
        size = 0
        current = head
        
        while current:
            size += 1
            current = current.next

        self.current = head

        # Helper function to build the BST recursively
        def convertListToBST(left, right):
            nonlocal size
            if left > right:
                return None

            mid = (left + right) // 2

            # Build the left subtree
            left_child = convertListToBST(left, mid - 1)

            # The middle node is the root at this level
            root = TreeNode(self.current.val)
            root.left = left_child

            # Move to the next list node
            self.current = self.current.next

            # Build the right subtree
            root.right = convertListToBST(mid + 1, right)

            return root

        # Build the BST using the helper function
        return convertListToBST(0, size - 1)

# Tests
def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

def is_balanced(root):
    def check(node):
        if not node:
            return True, 0  # is_balanced, height
        left_balanced, left_height = check(node.left)
        right_balanced, right_height = check(node.right)
        current_height = 1 + max(left_height, right_height)
        current_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        return current_balanced, current_height
    
    balanced, _ = check(root)
    return balanced

def inorder_traversal(root):
    result = []
    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
    traverse(root)
    return result

solution = Solution()

# Define test cases
test_cases = [
    [],  # empty list
    [1],  # single element
    [1, 2],  # two elements
    [1, 2, 3],  # three elements, perfect BST
    [-10, -3, 0, 5, 9],  # multiple elements, balanced BST
]

# Execute tests
for index, nums in enumerate(test_cases):
    print(f"Test Case {index + 1}: {nums}")
    head = create_linked_list(nums)
    tree = solution.sortedListToBST(head)
    balanced = is_balanced(tree)
    inorder = inorder_traversal(tree)
    print("Is balanced:", balanced)
    print("Inorder traversal:", inorder)
    print("Test Passed:", nums == inorder and balanced)
    print()
    
# Explanation
# 1. Find Middle:
# The function first identifies the middle node of the linked list segment. 
# This node becomes the root of the BST for the current recursive call. 
# This is crucial for ensuring the tree remains height-balanced, as it evenly divides the list into two halves.

# 2. Recursive Construction:
# - Build Left Subtree: The function recursively builds the left subtree using the left half of the linked list (nodes before the middle node). 
# This is achieved by another call to the function with the left segment of the list.
# - Build Right Subtree: Similarly, the function recursively builds the right subtree using the right half of the list (nodes after the middle node). 
# This ensures that all elements are properly placed in the BST according to their natural order in the list.

# 3. Return:
# Complete Node Formation: Once both left and right subtrees are constructed, the function attaches them to the left and right pointers of the middle node, which now serves as the root node for this part of the tree.
# Root Node Return: The current root node (middle node of the list segment) is returned to the previous recursive call (or as the final tree if this is the initial call). 
# This step is critical as it forms the linkage necessary to piece together the entire tree as recursion unwinds.