class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)
        half = []
        mid = ""

        for ch in sorted(freq.keys()):
            count = freq[ch]
            half.append(ch * (count // 2))
            if count % 2 == 1:
                mid = ch  
        
        left = "".join(half)
        return left + mid + left[::-1]
