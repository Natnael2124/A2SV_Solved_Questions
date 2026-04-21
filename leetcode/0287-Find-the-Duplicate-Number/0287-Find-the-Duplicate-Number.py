class Solution:
    def findDuplicate(self, nums):
        slow = fast = 0

        # finding intersection 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # find where the cycle begin
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow