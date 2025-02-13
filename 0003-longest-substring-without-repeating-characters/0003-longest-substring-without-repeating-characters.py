class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
            
        left = 0
        char_dict = defaultdict(int)
        max_sum = float("-inf")

        for right in range(len(s)):
            if s[right] in char_dict:
                char_dict[s[right]]+=1

                while char_dict[s[right]] > 1:

                    char_dict[s[left]] -=1

                    if char_dict[s[left]] == 0:
                        del char_dict[s[left]]
                        left+=1
                left+=1

            else:
                char_dict[s[right]]+=1
            max_sum = max(max_sum, right-left+1)
        return max_sum