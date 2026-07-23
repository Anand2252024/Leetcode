class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial
        
        # Create list of numbers [1, 2, ..., n]
        numbers = [str(i) for i in range(1, n + 1)]
        
        # Convert k to zero-based index
        k -= 1  
        
        result = []
        
        for i in range(n, 0, -1):
            # Determine index of current digit
            idx = k // factorial(i - 1)
            k %= factorial(i - 1)
            
            # Append chosen digit and remove from list
            result.append(numbers.pop(idx))
        
        return "".join(result)
