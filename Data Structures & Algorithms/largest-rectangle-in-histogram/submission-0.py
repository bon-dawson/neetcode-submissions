class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_max, right_max = [-1] * n, [n] * n
        st = []
        for i in range(n):
            while st and heights[st[-1]] > heights[i]:
                right_max[st.pop()] = i

            if st:
                left_max[i] = st[-1]

            st.append(i)
        
        print(left_max)
        print(right_max)
        
        ans = 0
        for i in range(n):
            ans = max(ans, heights[i] * (right_max[i] - left_max[i] - 1))

        return ans
