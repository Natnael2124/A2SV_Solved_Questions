class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low = 1
        high = position[-1] - position[0]

        def checker(x):
            count = m - 1
            froom = position[0] + x 
            for i in range(1,len(position)):
                
                if position[i] >= froom :
                    froom = position[i] + x
                    count -= 1
                if count == 0:
                    return True
            return False
            
                
        res = 0
        while low <= high:
            mid = (low + high) // 2

            if checker(mid):
                res = mid
                low = mid + 1

            else:
                high = mid - 1
        return res 
