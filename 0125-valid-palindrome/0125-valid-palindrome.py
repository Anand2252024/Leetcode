class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""

        for ch in s:
            if ch.isalnum():
                text += ch.lower()

        left = 0
        right = len(text) - 1

        while left < right:
            if text[left] != text[right]:
                return False
            left += 1
            right -= 1

        return True