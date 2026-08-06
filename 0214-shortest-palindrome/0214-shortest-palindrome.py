class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        
        rev = s[::-1]
        combined = s + "#" + rev
        
        # KMP prefix function
        lps = [0] * len(combined)
        for i in range(1, len(combined)):
            j = lps[i-1]
            while j > 0 and combined[i] != combined[j]:
                j = lps[j-1]
            if combined[i] == combined[j]:
                j += 1
            lps[i] = j
        
        # longest palindromic prefix length
        longest = lps[-1]
        
        # add reversed suffix in front
        return rev[:len(s)-longest] + s
