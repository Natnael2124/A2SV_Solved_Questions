class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n 
        
        for i in range(n):
            if colors[i] != -1:
                continue
            
            queue = deque([i])
            colors[i] = 0
            
            while queue:
                u = queue.popleft()
                
                for v in graph[u]:
                    if colors[v] == -1:
                        colors[v] = 1 - colors[u]
                        queue.append(v)
                    elif colors[v] == colors[u]:
               
                        return False
                        
        return True