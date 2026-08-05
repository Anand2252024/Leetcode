class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Step 1: Split by whitespace (handles multiple spaces automatically)
        words = s.strip().split()
        
        # Step 2: Reverse the list
        words.reverse()
        
        # Step 3: Join with single space
        return " ".join(words)
