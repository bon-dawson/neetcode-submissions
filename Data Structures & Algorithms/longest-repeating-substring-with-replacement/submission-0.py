class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, ans, n = 0, 0, len(s)
        cnt = Counter()
        for r in range(n):
            cnt[s[r]] += 1
            while r - l + 1 - cnt.most_common(1)[0][1] > k:
                cnt[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans