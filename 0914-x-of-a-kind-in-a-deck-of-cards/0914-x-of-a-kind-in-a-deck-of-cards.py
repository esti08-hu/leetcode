class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq = {}

        for card in deck:
            freq[card] = freq.get(card, 0) + 1
        
        overall_gcd = reduce(gcd, freq.values())

        return overall_gcd > 1