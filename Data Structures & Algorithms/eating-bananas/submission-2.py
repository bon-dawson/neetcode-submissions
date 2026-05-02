class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, 10**9
        while l < r:
            m = (l + r) >> 1
            tot = 0
            for pile in piles:
                tot += (pile + m - 1) // m
            
            if tot <= h:
                r = m
            else:
                l = m + 1

        return r