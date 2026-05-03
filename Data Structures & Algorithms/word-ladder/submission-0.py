class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        words, ans = set(wordList), 0
        q = deque([beginWord])

        while q:
            ans += 1
            for _ in range(len(q)):
                node = q.popleft()

                if node == endWord:
                    return ans

                for i in range(len(node)):
                    for j in range(26):
                        c = chr(j + 97)
                        if c == node[i]:
                            continue
                        nei = node[:i] + c + node[i + 1:]
                        if nei in words:
                            q.append(nei)
                            words.remove(nei)

        return 0