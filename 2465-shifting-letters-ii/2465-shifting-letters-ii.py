class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        pre = [0]*(n+1)

        for l,r,d in shifts:
            if d == 0:
                d = -1

            if r+1 < n:
                pre[r+1] -= d
            
            pre[l] += d

        pre_sum = [0]*n
        pre_sum[0] = pre[0]

        for i in range(1, n):
            pre_sum[i] = pre[i] + pre_sum[i-1]

        s = list(s)
    for i in range(n):
        # Calculate shift value based on the prefix sum, wrapping around using modulo 26
        shift = pre_sum[i] % 26
        
        # Get the current position of the character in the alphabet
        pos = ord(s[i]) - ord("a")
        
        # Calculate the new position after applying the shift, also wrapping around
        shift_pos = (pos + shift) % 26
        
        # Convert the new position back to a character
        new_char = chr(shift_pos + ord("a"))
        
        s[i] = new_char


        return "".join(s)