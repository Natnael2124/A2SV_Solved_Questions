class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        def power(m):
            if m == 0:
                return 1
            
            half = (power(m//2)) % mod

            if m %2 == 0 :
                return half * half
            else:
                return half * half * 20

        if n%2 ==1:
            return (power(n//2) *5) % mod
        else:
            return (power(n//2)) % mod

