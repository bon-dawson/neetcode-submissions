class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        shown = defaultdict(bool)
        for num in nums:
            if shown[num]:
                return True
            shown[num] = True
        return False