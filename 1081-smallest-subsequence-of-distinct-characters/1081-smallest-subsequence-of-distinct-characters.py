class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Count how many times each character appears
        last_occurrence = {c: i for i, c in enumerate(s)}
        
        stack = []
        seen = set()
        
        for i, c in enumerate(s):
            # If character already in stack, skip it
            if c in seen:
                continue
            
            # Maintain lexicographic order
            while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                removed = stack.pop()
                seen.remove(removed)
            
            stack.append(c)
            seen.add(c)
        
        return "".join(stack)
