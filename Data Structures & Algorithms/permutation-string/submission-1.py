class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        cnt1, cnt2 = [0] * 26, [0] * 26
        for i in range(n):
            cnt1[ord(s1[i]) - ord('a')] += 1
            cnt2[ord(s2[i]) - ord('a')] += 1

        match = 0
        for i in range(26):
            if cnt1[i] == cnt2[i]:
                match += 1

        for i in range(n, m):
            if match == 26:
                return True

            r = ord(s2[i]) - ord('a')
            cnt2[r] += 1
            if cnt2[r] == cnt1[r]:
                match += 1
            elif cnt2[r] == cnt1[r] + 1:
                match -= 1

            l = ord(s2[i - n]) - ord('a')
            cnt2[l] -= 1
            if cnt2[l] == cnt1[l]:
                match += 1
            elif cnt2[l] == cnt1[l] - 1:
                match -= 1

        print(match)

        return match == 26