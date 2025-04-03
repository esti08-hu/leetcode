# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        curr = head
        vals = []
        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        vals.sort()
        head = ListNode(vals[0])
        curr = head
        for i in range(1, len(vals)):
            curr.next = ListNode(vals[i])
            curr = curr.next
        
        return head


                


