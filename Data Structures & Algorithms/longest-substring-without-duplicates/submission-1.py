class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        l, r, n = 0, 0, len(s)
        ans = 0
        while r < n:
            while s[r] in st:
                st.remove(s[l])
                l += 1
            ans = max(ans, r - l + 1)
            st.add(s[r])
            r += 1

        return ans