# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1]*n for _ in range(m)]
        r, c = 0, 0 
        def inBound(r, c):
            return 0 <= r < m and 0 <= c < n
        curr = head
        mat[0][0] = curr.val
        while curr.next:
            #right
            while inBound(r, c+1) and curr.next and mat[r][c+1] == -1:
                c += 1
                curr = curr.next
                mat[r][c] = curr.val
            
            #down
            while inBound(r+1, c) and curr.next and mat[r+1][c] == -1:
                r += 1
                curr = curr.next
                mat[r][c] = curr.val
            
            #left
            while inBound(r, c-1) and curr.next and mat[r][c-1] == -1:
                c -= 1 
                curr = curr.next
                mat[r][c] = curr.val
            
            #up
            while inBound(r-1, c) and curr.next and mat[r-1][c] == -1:
                r -= 1
                curr = curr.next
                mat[r][c] = curr.val
        
        return mat