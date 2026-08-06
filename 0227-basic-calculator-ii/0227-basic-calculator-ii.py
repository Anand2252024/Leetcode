class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        stack = []
        num = 0
        op = '+'
        
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if not ch.isdigit() or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    prev = stack.pop()
                    # truncate toward zero
                    stack.append(int(prev / float(num)))
                op = ch
                num = 0
        
        return sum(stack)
