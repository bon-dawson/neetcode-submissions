class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        reached = [0]
        n = len(s)
        for i in range(n):
            if s[i] == '1':
                continue
            
            left = i - maxJump
            right = i - minJump

            if right < 0:
                continue

            l, r = 0, len(reached)
            while l < r:
                m = (l + r) >> 1
                if reached[m] < left:
                    l = m + 1
                else:
                    r = m

            if l < len(reached) and reached[l] <= right:
                reached.append(i)

                
        return len(s) - 1 in reached