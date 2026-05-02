class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
    
    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.add_word(w)

        ROWS, COLS = len(board), len(board[0])
        res, vis = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                (r, c) in vis or board[r][c] not in node.children):
                return

            vis.add((r,c))
            word += board[r][c]
            node = node.children[board[r][c]]

            if node.end_of_word:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c - 1, node, word)

            vis.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)