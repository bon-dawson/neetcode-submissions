class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        cnt1, cnt2 = defaultdict(int), defaultdict(int)
        for c in t:
            cnt2[c] += 1

        mx, ans = float("inf"), [-1, -1]
        cur, target = 0, len(t)
        l = 0
        for r in range(n):
            c = s[r]
            cnt1[c] += 1
            if c in t and cnt1[c] == cnt2[c]:
                cur += 1

            while cur == target:
                if r - l + 1 < mx:
                    mx = r - l + 1
                    ans = [l, r]

                x = s[l]
                cnt1[x] -= 1
                if x in t and cnt1[x] + 1 == cnt2[x]:
                    cur -= 1
                l += 1

        l, r = ans
        return s[l: r + 1] if mx != float("inf") else ""