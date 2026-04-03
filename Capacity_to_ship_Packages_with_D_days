class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(capacity):
            weight_sum = 0
            day = 1

            for i in weights:
                weight_sum += i
                
                if weight_sum > capacity:
                    weight_sum = i
                    day += 1
                if day > days:
                    return False
            return True
        
        high = sum(weights)
        low = max(weights)

        while low <= high:
            mid = (low + high) // 2

            if check(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
        
