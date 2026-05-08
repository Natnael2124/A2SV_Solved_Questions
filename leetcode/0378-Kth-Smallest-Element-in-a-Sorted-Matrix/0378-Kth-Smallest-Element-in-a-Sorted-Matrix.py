import heapq

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        # min_heap stores (value, row_index, col_index)
        # We only need to start with the first element of each row
        min_heap = []
        
        # Optimization: We only need at most k rows if k < n
        for r in range(min(n, k)):
            heapq.heappush(min_heap, (matrix[r][0], r, 0))
        
        val = 0
        for _ in range(k):
            val, r, c = heapq.heappop(min_heap)
            
            # If there's a next element in the current row, add it to the heap
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
                
        return val