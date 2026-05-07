class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = [[] for _ in range(n + 1)]
        in_degree = [0] * (n + 1)
        for prev, next_c in relations:
            adj[prev].append(next_c)
            in_degree[next_c] += 1
        
        # earliest_finish[i] stores the max time to complete all paths ending at course i
        earliest_finish = [0] * (n + 1)
        queue = deque()
        
        # Initialize queue with courses having no prerequisites
        for i in range(1, n + 1):
            if in_degree[i] == 0:
                queue.append(i)
                earliest_finish[i] = time[i - 1]
        
        while queue:
            curr = queue.popleft()
            
            for neighbor in adj[curr]:
                # Update neighbor's completion time: 
                # max(current_stored_time, curr_finish_time + neighbor_duration)
                earliest_finish[neighbor] = max(
                    earliest_finish[neighbor], 
                    earliest_finish[curr] + time[neighbor - 1]
                )
                
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return max(earliest_finish)