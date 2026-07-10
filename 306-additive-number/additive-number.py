class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            for j in range(i + 1, n):

                # Leading zero check
                if num[0] == '0' and i > 1:
                    break
                if num[i] == '0' and j - i > 1:
                    continue

                a = int(num[:i])
                b = int(num[i:j])

                k = j
                while k < n:
                    s = str(a + b)
                    if not num.startswith(s, k):
                        break
                    k += len(s)
                    a, b = b, a + b

                if k == n:
                    return True

        return False