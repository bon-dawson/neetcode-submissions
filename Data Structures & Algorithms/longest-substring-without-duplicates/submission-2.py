class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     st = set()
    #     l, r, n = 0, 0, len(s)
    #     ans = 0
    #     while r < n:
    #         while s[r] in st:
    #             st.remove(s[l])
    #             l += 1
    #         ans = max(ans, r - l + 1)
    #         st.add(s[r])
    #         r += 1

    #     return ans
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp_idx = {}
        ans, l = 0, 0
        for r in range(len(s)):
            if s[r] in mp_idx:
                l = max(l, mp_idx[s[r]] + 1)
            ans = max(ans, r - l + 1)
            mp_idx[s[r]] = r
        return ans