class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        res = []
        for x in nums:
            # Use the value as an index (mapped to 0-based)
            idx = abs(x) - 1
            if nums[idx] < 0:
                # If already negative, we've seen this value before
                res.append(abs(x))
            else:
                # Mark as seen by negating the value at that index
                nums[idx] *= -1
        return res