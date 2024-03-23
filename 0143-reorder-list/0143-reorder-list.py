# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        middle = self.findMiddle(head)
        
        second_half = middle.next
        middle.next = None
       
        reversed_second_half = self.reverseList(second_half)
        
        self.mergeLists(head, reversed_second_half)
    
    def findMiddle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def mergeLists(self, l1: ListNode, l2: ListNode) -> None:
        while l1 and l2:
            next_l1 = l1.next
            next_l2 = l2.next
            
            l1.next = l2
            l2.next = next_l1
            
            l1 = next_l1
            l2 = next_l2