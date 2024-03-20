# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        node_before_range = None
        node_after_range = None
        curr = list1
        pos = 0
        while curr:
            if pos == a - 1:
                node_before_range = curr
            if pos == b + 1:
                node_after_range = curr
                break
            curr = curr.next
            pos += 1
        
        node_before_range.next = list2
        curr = list2
        while curr.next:
            curr = curr.next
        
        curr.next = node_after_range
        
        return list1