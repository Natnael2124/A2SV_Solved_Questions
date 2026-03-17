class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        tar = target
        count = 0
        for i in range(maxDoubles):
            if tar <= 1:
                return count
            else:
                if tar % 2 == 0:
                    count += 1
                    tar = tar // 2
                else:
                    count += 2
                    tar = tar // 2
        return count + tar -1

