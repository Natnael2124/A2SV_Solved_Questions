class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def sub(i,num):
            if num not in res:
                res.append(num[:])

            if i == len(nums) :
                return
            
            for j in range(i,len(nums)):
                num.append(nums[j])
                i += 1
                sub(i,num)
                num.pop()
                

        sub(0,[])
        
        return res
