class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        
        def backtrack(index, path, value, last):
            # index: current position in num
            # path: expression built so far
            # value: evaluated result so far
            # last: last operand (for multiplication correction)
            
            if index == len(num):
                if value == target:
                    res.append(path)
                return
            
            for i in range(index, len(num)):
                # avoid leading zeros
                if i != index and num[index] == '0':
                    break
                curr_str = num[index:i+1]
                curr = int(curr_str)
                
                if index == 0:
                    # first number, no operator
                    backtrack(i+1, curr_str, curr, curr)
                else:
                    # addition
                    backtrack(i+1, path + "+" + curr_str, value + curr, curr)
                    # subtraction
                    backtrack(i+1, path + "-" + curr_str, value - curr, -curr)
                    # multiplication
                    backtrack(i+1, path + "*" + curr_str, value - last + last * curr, last * curr)
        
        backtrack(0, "", 0, 0)
        return res
