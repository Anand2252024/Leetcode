class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # Check whether a palindrome is possible
        odd = -1
        for i in range(26):
            if cnt[i] % 2:
                if odd != -1:
                    return ""
                odd = i

        # Characters used in the left half
        half = [x // 2 for x in cnt]
        m = n // 2

        def make_pal(left):
            middle = chr(odd + ord('a')) if odd != -1 else ""
            return left + middle + left[::-1]

        # Smallest possible palindrome
        left = []
        for i in range(26):
            left.extend([chr(i + ord('a'))] * half[i])

        smallest = ''.join(left)
        ans = make_pal(smallest)

        if ans > target:
            return ans

        prefix_target = target[:m]

        # --------------------------------------------------
        # IMPORTANT:
        # Check whether target[:m] itself can be the left half.
        # The resulting palindrome may still be > target.
        # --------------------------------------------------
        rem = half[:]
        possible = True

        for ch in prefix_target:
            c = ord(ch) - ord('a')

            if rem[c] == 0:
                possible = False
                break

            rem[c] -= 1

        if possible:
            candidate = make_pal(prefix_target)

            if candidate > target:
                return candidate

        # --------------------------------------------------
        # Find the smallest left half strictly greater than
        # target[:m]
        # --------------------------------------------------
        for i in range(m - 1, -1, -1):
            rem = half[:]
            prefix = []
            possible = True

            # Match target prefix before position i
            for j in range(i):
                c = ord(prefix_target[j]) - ord('a')

                if rem[c] == 0:
                    possible = False
                    break

                rem[c] -= 1
                prefix.append(chr(c + ord('a')))

            if not possible:
                continue

            # Choose the smallest character greater than target[i]
            current = ord(prefix_target[i]) - ord('a')
            chosen = -1

            for c in range(current + 1, 26):
                if rem[c] > 0:
                    chosen = c
                    break

            if chosen == -1:
                continue

            rem[chosen] -= 1
            prefix.append(chr(chosen + ord('a')))

            # Fill remaining positions with smallest characters
            for c in range(26):
                if rem[c]:
                    prefix.extend([chr(c + ord('a'))] * rem[c])

            left = ''.join(prefix)
            candidate = make_pal(left)

            if candidate > target:
                return candidate

        return ""