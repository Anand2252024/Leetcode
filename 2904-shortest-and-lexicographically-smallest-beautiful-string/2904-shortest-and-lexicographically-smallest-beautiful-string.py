class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        ans = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            if ones == k:
                # Remove unnecessary leading zeros
                while left <= right and s[left] == '0':
                    left += 1

                current = s[left:right + 1]

                if ans == "" or len(current) < len(ans) or \
                   (len(current) == len(ans) and current < ans):
                    ans = current

        return ans