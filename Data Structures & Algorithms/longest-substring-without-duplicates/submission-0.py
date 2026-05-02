class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev_idx = defaultdict(lambda: -1)
        ans, cnt, i = 0, 0, 0
        n = len(s)
        for j in range(n):
            if prev_idx[s[j]] != -1:
                while prev_idx[s[j]] != -1:
                    prev_idx[s[i]] = -1
                    i += 1
            else:
                ans = max(ans, j - i + 1)

            prev_idx[s[j]] = j
        return ans