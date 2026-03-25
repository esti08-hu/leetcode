# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        curr = head

        while curr.next:
            if curr.val == float("inf"):
                return True
            curr.val = float("inf")
            curr = curr.next
        
        return False