class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        right = defaultdict(int)
        ans = defaultdict(list)
        for i in nums:
            right[i] += 1

        score = right[1]
        ans[score].append(0)
        new = score

        for j in range(len(nums)):
            if nums[j] == 0:
                new += 1

            elif nums[j] == 1:
                new -= 1

            if new > score:
                score = new
                ans[score] = [j + 1]

            elif new == score:
                ans[score].append(j + 1)
        
        return ans[score]
