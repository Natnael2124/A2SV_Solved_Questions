class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_d = deque()
        min_d = deque()
        left = 0
        max_len = 0

        for r in range(len(nums)):
            while max_d and max_d[-1] < nums[r]:
                max_d.pop()
            max_d.append(nums[r])
            while min_d and min_d[-1] > nums[r]:
                min_d.pop()
            min_d.append(nums[r])

            while  max_d[0] - min_d[0] > limit:
                if max_d[0] == nums[left]:
                    max_d.popleft()
                if min_d[0] == nums[left]:
                    min_d.popleft()
                
                left += 1

            max_len = max(max_len, r - left +1)
        return max_len

