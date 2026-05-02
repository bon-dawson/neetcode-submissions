import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = (l + r) >> 1
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        pivot = l
        left = bisect.bisect_left(nums[:pivot], target)
        if left < n and nums[left] == target:
            return left
        right = pivot + bisect.bisect_left(nums[pivot:], target)
        if right < n and nums[right] == target:
            return right

        print(left, right)
        return -1
