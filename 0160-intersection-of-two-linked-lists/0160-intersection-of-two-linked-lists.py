# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list_set = set()

        while headA:
            list_set.add(headA)
            headA =  headA.next
        
        while headB:
            if headB in list_set:
                return headB
            headB = headB.next

        

