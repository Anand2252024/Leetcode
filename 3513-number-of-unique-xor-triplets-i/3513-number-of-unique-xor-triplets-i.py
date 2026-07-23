class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        
        # For small n, brute force is fine
        if n <= 20:
            seen = set()
            for i in range(n):
                for j in range(i, n):
                    for k in range(j, n):
                        seen.add(nums[i] ^ nums[j] ^ nums[k])
            return len(seen)
        
        # For large n, the XOR space fills completely
        return 1 << (n.bit_length())
