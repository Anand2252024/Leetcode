class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        memo = {}
        
        def helper(expr):
            if expr in memo:
                return memo[expr]
            
            results = []
            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left = helper(expr[:i])
                    right = helper(expr[i+1:])
                    for l in left:
                        for r in right:
                            if ch == '+':
                                results.append(l + r)
                            elif ch == '-':
                                results.append(l - r)
                            else:  # '*'
                                results.append(l * r)
            
            if not results:  # expr is a number
                results = [int(expr)]
            
            memo[expr] = results
            return results
        
        return helper(expression)
