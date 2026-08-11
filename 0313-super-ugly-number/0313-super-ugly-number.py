class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)

        ugly = [1] * n
        idx = [0] * k
        values = primes[:]

        for i in range(1, n):
            nxt = min(values)
            ugly[i] = nxt

            for j in range(k):
                if values[j] == nxt:
                    idx[j] += 1
                    values[j] = primes[j] * ugly[idx[j]]

        return ugly[-1]