class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_max, right_max = [-1] * n, [n] * n
        st = []
        for i in range(n):
            while st and heights[st[-1]] > heights[i]:
                right_max[st[-1]] = i
                st.pop()
            
            if st:
                left_max[i] = st[-1]
            
            st.append(i)

        ans = 0
        for i in range(n):
            ans = max(ans, heights[i] * (right_max[i] - left_max[i] - 1))
        return ans