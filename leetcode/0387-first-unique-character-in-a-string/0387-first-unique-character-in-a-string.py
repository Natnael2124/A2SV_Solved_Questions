class Solution:
    def firstUniqChar(self, s: str) -> int:
        duplicate = []
        length = len(s)
        if length == 1:
            return 0
        else:

            for i in range(len(s)):
                if i == len(s) - 1 and s[i] not in duplicate:
                    return len(s) - 1
                for j in range(i+1,len(s)):
                    if s[i] == s[j]:
                        duplicate.append(s[i])
                        break
                    elif s[i] in duplicate:
                        break
                        
                    
                    elif j == len(s)-1:
                        return i
                
                
            return -1