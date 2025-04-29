# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, l in enumerate(lists):
            if l:
                heappush(heap, (l.val, i, l))

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i, node = heappop(heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
        
        
