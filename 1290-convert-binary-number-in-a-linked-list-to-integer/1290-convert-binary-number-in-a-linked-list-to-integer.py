# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        def convertToInt(binary):
            total = 0
            for i in range(len(binary)):
                if binary[i]:
                    total += 2**i
            return total
        res = []

        curr =  head
        while curr:
            res.append(curr.val)
            curr = curr.next
        
        return convertToInt(res[::-1])