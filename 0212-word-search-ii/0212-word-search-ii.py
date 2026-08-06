class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # store complete word at end node

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # Build Trie
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w
        
        m, n = len(board), len(board[0])
        result = []
        
        def dfs(i, j, node):
            ch = board[i][j]
            if ch not in node.children:
                return
            nxt = node.children[ch]
            if nxt.word:
                result.append(nxt.word)
                nxt.word = None  # avoid duplicates
            
            board[i][j] = "#"  # mark visited
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] != "#":
                    dfs(x, y, nxt)
            board[i][j] = ch  # restore
            
            # prune empty nodes
            if not nxt.children:
                node.children.pop(ch)
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        
        return result
