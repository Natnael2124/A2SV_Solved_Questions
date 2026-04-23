class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maxx = 0
        j = 1
        i = 0
        while j < len(nums):
            maxx = max(nums[j]-nums[i], maxx)
            i += 1
            j += 1
        return maxx