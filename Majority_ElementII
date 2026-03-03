class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)//3
        count=Counter(nums)
        output=[]
        for i in count:
            if count[i]>n:
                output.append(i)
        return output
        
        
