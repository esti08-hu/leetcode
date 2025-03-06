# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head

        fast=head 
        slow=head 
        left = []
        right = []
        while fast and fast.next:
            left.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        
        while slow:
            right.append(slow.val)
            slow = slow.next
        right = right[::-1]

        return max(left[i]+right[i] for i in range(len(right)))


