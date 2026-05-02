class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans

    def decode(self, s: str) -> List[str]:
        i, n = 0, len(s)
        ans = []
        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            
            s_len = int(s[i:j])
            i = j + 1 + s_len

            ans.append(s[j + 1 : i])

        return ans