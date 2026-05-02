class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        st = []
        for c in s:
            if c in mp:
                if not st or st[-1] != mp[c]:
                    return False
                st.pop()
            else:
                st.append(c)
            
        return True