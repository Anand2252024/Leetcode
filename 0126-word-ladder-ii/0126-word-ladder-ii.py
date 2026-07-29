from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        parents = defaultdict(list)
        level = {beginWord}
        found = False

        while level and not found:
            nextLevel = set()

            for word in level:
                wordSet.discard(word)

            for word in level:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + c + word[i + 1:]

                        if newWord in wordSet:
                            parents[newWord].append(word)
                            nextLevel.add(newWord)

                            if newWord == endWord:
                                found = True

            level = nextLevel

        result = []

        def dfs(word, path):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                dfs(parent, path + [parent])

        if found:
            dfs(endWord, [endWord])

        return result