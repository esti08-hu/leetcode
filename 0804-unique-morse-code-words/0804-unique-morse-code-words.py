class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = set()

        for word in words:
            curr_word = []
            for w in word:
                idx = ord(w) - ord("a")
                curr_word.append(morse[idx])
            res.add("".join(curr_word))
        
        return len(res)
