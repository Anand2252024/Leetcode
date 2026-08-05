class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        repeated = set()
        
        for i in range(len(s) - 9):  # window size = 10
            substring = s[i:i+10]
            if substring in seen:
                repeated.add(substring)
            else:
                seen.add(substring)
        
        return list(repeated)
