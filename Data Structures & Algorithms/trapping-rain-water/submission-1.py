class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        suff = [0] * n
        suff[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = max(suff[i + 1], height[i])
        print(suff)
        
        max_left = 0
        ans = 0
        for i in range(n - 1):
            diff = min(max_left, suff[i + 1]) - height[i]
            print(diff)
            if diff > 0:
                ans += diff
            max_left = max(max_left, height[i])

        return ans