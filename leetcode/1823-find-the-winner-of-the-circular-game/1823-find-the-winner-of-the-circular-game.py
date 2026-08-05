class Solution:
    def findTheWinner(self, n: int, k: int) -> int: 
        circle = list(range(1,n+1))

        start_indx = 0

        while len(circle) > 1:
            removal_indx =  (start_indx + k - 1) % len(circle)

            circle.pop(removal_indx)

            start_indx = removal_indx
            
        return circle[0]
