class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        ans = [intervals[0]]
        for start, end in intervals:
            last_end = ans[-1][1]

            if last_end >= start:
                ans[-1][1] = max(last_end, end)
            else:
                ans.append([start, end])

        return ans