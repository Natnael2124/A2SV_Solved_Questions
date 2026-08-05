class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        fir = 0
        sec = fir + 1
        
        while sec <= len(nums) - 1:
            if nums[fir] == nums[sec]:
                nums[fir] = nums[fir] * 2
                nums[sec] = 0

            fir += 1
            sec += 1
        
        read = 0 
        write = 0

        while read < len(nums):
            if nums[read] != 0:
                temp = nums[read]
                nums[read] = nums[write]
                nums[write] = temp

                write = write + 1
            read += 1
        
        return nums