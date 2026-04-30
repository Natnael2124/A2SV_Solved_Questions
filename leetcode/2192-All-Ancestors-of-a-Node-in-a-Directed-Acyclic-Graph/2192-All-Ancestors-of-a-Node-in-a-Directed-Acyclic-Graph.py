class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n

        for dad , son in edges:
            graph[dad].append(son)
            indegree[son] += 1

        queue = deque(i for i in range(n) if indegree[i] == 0)
        tbs = []

        while queue:
            u = queue.popleft()
            tbs.append(u)

            for j in graph[u]:
                indegree[j] -= 1 
                if indegree[j] == 0:
                    queue.append(j)

        ancestorlist = [[] for _ in range(n)]
        ancestorset = [set() for _ in range(n)]

        for node in tbs:
            for child in graph[node]:
                ancestorset[child].add(node)
                ancestorset[child].update(ancestorset[node])

        for i in range(n):
            for node in range(n):
                if node == i:
                    continue
                if node in ancestorset[i]:
                    ancestorlist[i].append(node) 

        return ancestorlist