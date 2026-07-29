from collections import Counter
from string import ascii_lowercase

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        freq = Counter(s)
        mid = ""
        half = []
        
        # Identify middle character if odd count
        for ch, count in freq.items():
            if count % 2 == 1:
                if mid: return ""  # more than one odd → impossible
                mid = ch
            half.extend([ch] * (count // 2))
        
        freq_half = Counter(half)
        half_len = len(half)

        # helper: count permutations of multiset
        def count_perms(freq, rem):
            res = 1
            for c, cnt in freq.items():
                if cnt == 0: continue
                m = min(cnt, rem - cnt)
                val = 1
                for i in range(1, m+1):
                    val = val * (rem - i + 1) // i
                    if val > k: return val  # early stop
                res *= val
                if res > k: return res
                rem -= cnt
            return res

        total = count_perms(freq_half, half_len)
        if k > total: return ""

        # build k-th half
        half_str = []
        for pos in range(half_len):
            for c in ascii_lowercase:
                if freq_half[c] == 0: continue
                freq_half[c] -= 1
                cnt = count_perms(freq_half, half_len - pos - 1)
                if k <= cnt:
                    half_str.append(c)
                    break
                else:
                    k -= cnt
                    freq_half[c] += 1

        half_str = "".join(half_str)
        return half_str + mid + half_str[::-1]
