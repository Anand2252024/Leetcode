class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        memo = {}
        def dfs(start):
            if start == len(s):
                return [""]
            if start in memo:
                return memo[start]
            ans = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in words:
                    rest = dfs(end)
                    for sentence in rest:
                        if sentence == "":
                            ans.append(word)
                        else:
                            ans.append(word + " " + sentence)
            memo[start] = ans
            return ans
        return dfs(0)