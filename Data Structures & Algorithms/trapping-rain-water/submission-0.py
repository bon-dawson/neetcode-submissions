class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        suff = [0] * n
        for i in range(n - 2, -1, -1):
            suff[i] = max(suff[i + 1], height[i])
        
        max_left = 0
        ans = 0
        for i in range(n - 1):
            ans += max(height[i], min(max_left, suff[i + 1])) - height[i]
            max_left = max(max_left, height[i])

        return ans