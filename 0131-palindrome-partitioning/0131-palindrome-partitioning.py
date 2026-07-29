class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result = []

        def isPalindrome(word):
            return word == word[::-1]

        def backtrack(start, path):

            if start == len(s):
                result.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):

                part = s[start:end]

                if isPalindrome(part):
                    path.append(part)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])

        return result