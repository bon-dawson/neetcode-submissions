class Solution:
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     if endWord not in wordList or beginWord == endWord:
    #         return 0

    #     words, ans = set(wordList), 0
    #     q = deque([beginWord])

    #     while q:
    #         ans += 1
    #         for _ in range(len(q)):
    #             node = q.popleft()

    #             if node == endWord:
    #                 return ans

    #             for i in range(len(node)):
    #                 for j in range(26):
    #                     c = chr(j + 97)
    #                     if c == node[i]:
    #                         continue
    #                     nei = node[:i] + c + node[i + 1:]
    #                     if nei in words:
    #                         q.append(nei)
    #                         words.remove(nei)

    #     return 0
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                nei[pattern].append(word)

        q = deque([beginWord])
        visit = set([beginWord])
        ans = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return ans

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)

            ans += 1

        return 0