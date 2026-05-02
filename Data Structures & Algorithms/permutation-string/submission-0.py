class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1, cnt2 = Counter(s1), Counter()
        l, n = 0, len(s2)
        for r in range(n):
            cnt2[s2[r]] += 1
            while l <= r and cnt2[s2[r]] > cnt1[s2[r]]:
                cnt2[s2[l]] -= 1
                l += 1
            if cnt1 == cnt2:
                return True
        return False