class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        ans = []
        for values in reversed(cnt):
            if k > 0:
                ans.append(values)
            k -= 1
        return ans