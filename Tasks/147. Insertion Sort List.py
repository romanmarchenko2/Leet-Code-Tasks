# Link
# https://leetcode.com/problems/insertion-sort-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        # No need to sort for empty list or list of size 1
        if not head or not head.next:
            return head
        
        # Use dummy_head will help us to handle insertion before head easily
        dummy_head = ListNode(float('-inf'), next=head)
        last_sorted = head # last node of the sorted part
        cur = head.next # cur is always the next node of last_sorted
        
        while cur:
            if cur.val >= last_sorted.val:
                last_sorted = last_sorted.next
            else:
                # Search for the position to insert
                prev = dummy_head
                while prev.next.val <= cur.val:
                    prev = prev.next
                    
                # Insert
                last_sorted.next = cur.next
                cur.next = prev.next
                prev.next = cur
                
            cur = last_sorted.next
            
        return dummy_head.next
    
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

node1 = ListNode(4)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node4

print("Невідсортований список:")
print_list(node1)

solution = Solution()
sorted_head = solution.insertionSortList(node1)

print("Відсортований список:")
print_list(sorted_head)

# Explantaion
# 1. Add dummy_head before head will help us to handle the insertion easily

# 2. Use two pointers
# - last_sorted: last node of the sorted part, whose value is the largest of the sorted part
# - cur: next node of last_sorted, which is the current node to be considered

# At the beginning, last_sorted is head and cur is head.next

# 3. When consider the cur node, there're 2 different cases
# - last_sorted.val <= cur.val: cur is in the correct order and can be directly move into the sorted part. In this case, we just move last_sorted one step forward
# - last_sorted.val > cur.val: cur needs to be inserted somewhere in the sorted part. 
# In this case, we let prev start from dummy_head and iteratively compare prev.next.val and cur.val. If prev.next.val > cur.val, we insert cur between prev and prev.next
