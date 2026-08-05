class Solution:
    def reverseString(self, s: List[str]) -> None:
        first = 0
        second = len(s) - 1
        while first < second:
            s[first] , s[second] = s[second], s[first]
            first += 1
            second -= 1
        return s
        