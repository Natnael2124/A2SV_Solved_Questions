class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = {}

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i + j not in d:
                    d[i+j] = [mat[i][j]]
                else:
                    d[i+j].append(mat[i][j])
        
        ans = []

        for digsum in d:
            if digsum % 2 == 0:
                ans.extend(d[digsum][::-1])
            else:
                ans.extend(d[digsum])
        return ans


        