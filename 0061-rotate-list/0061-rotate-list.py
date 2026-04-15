# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return 

        node_num = 0

        curr = head
        while curr:
            node_num += 1
            curr = curr.next
        if node_num == 1:
            return head

        k = k % node_num
        if k == 0:
            return head

        x = node_num - k

        curr = head
        i = 1
        while curr and i < x:
            i += 1
            curr = curr.next

        new_head = curr.next
        curr.next = None

        curr = new_head
        while curr and curr.next:
            curr = curr.next
        
        curr.next = head

        return new_head




