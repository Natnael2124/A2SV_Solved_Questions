class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low, mid = 0, 0
        high = len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap 0 to the low boundary
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 is already in the 'middle', just move on
                mid += 1
            else: # nums[mid] == 2
                # Swap 2 to the high boundary
                nums[mid], nums[high] = nums[high], nums[mid]
                # Do NOT increment mid here; we need to inspect the 
                # new value swapped from the end.
                high -= 1