class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        node_before_range = list1
        for _ in range(a - 1):
            node_before_range = node_before_range.next
        node_after_range = node_before_range
        for _ in range(b - a + 2):
            node_after_range = node_after_range.next
            
        node_before_range.next = list2
        
        curr = list2
        while curr.next:
            curr = curr.next
            
        curr.next = node_after_range
        
        return list1