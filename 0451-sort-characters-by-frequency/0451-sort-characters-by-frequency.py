class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Count frequency of each character
        freq = Counter(s)
        
        # Sort characters by frequency (descending)
        sorted_chars = sorted(freq.items(), key=lambda x: -x[1])
        
        # Build the result string
        result = "".join([char * count for char, count in sorted_chars])
        
        return result
