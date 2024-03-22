from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        
        #find the middle of the list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        #reverse the half list
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        #check palendrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            else:
                left = left.next
                right = right.next
        return True
        
        
        
            
        