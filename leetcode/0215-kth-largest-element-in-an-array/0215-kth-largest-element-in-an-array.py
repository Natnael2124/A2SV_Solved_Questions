class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_no = max(nums)
        min_no = min(nums)
        hashmap = Counter(nums)
        count = 0

        for i in range(max_no,min_no - 1,-1):
            count += hashmap[i]
            if count >= k:
                return i

