class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # Split into revisions
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        # Find max length
        n = max(len(v1), len(v2))
        
        # Compare revisions one by one
        for i in range(n):
            # Convert to int, pad with 0 if missing
            num1 = int(v1[i]) if i < len(v1) else 0
            num2 = int(v2[i]) if i < len(v2) else 0
            
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        
        # All revisions equal
        return 0
