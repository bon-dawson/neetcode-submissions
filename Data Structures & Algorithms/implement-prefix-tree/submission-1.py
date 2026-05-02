# class TrieNode:
#     def __init__(self):
#         self.children = [None] * 26
#         self.end_of_word = False

# class PrefixTree:

#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word: str) -> None:
#         cur = self.root
#         for c in word:
#             i = ord(c) - ord('a')
#             if cur.children[i] == None:
#                 cur.children[i] = TrieNode()
#             cur = cur.children[i]
#         cur.end_of_word = True

#     def search(self, word: str) -> bool:
#         cur = self.root
#         for c in word:
#             i = ord(c) - ord('a')
#             if cur.children[i] == None:
#                 return False
#             cur = cur.children[i]
        
#         return cur.end_of_word

#     def startsWith(self, prefix: str) -> bool:
#         cur = self.root
#         for c in prefix:
#             i = ord(c) - ord('a')
#             if cur.children[i] == None:
#                 return False
#             cur = cur.children[i]
#         return True

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end_of_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True