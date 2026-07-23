class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        res = []
        
        # Generate all sequential numbers
        for length in range(2, 10):  # length of substring
            for start in range(0, 10 - length):
                num = int(s[start:start+length])
                if low <= num <= high:
                    res.append(num)
        
        return sorted(res)
