from collections import defaultdict

class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)

        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))

        visited = set()
        ans = float("inf")

        def dfs(node):
            visited.add(node)
            for nei, d in graph[node]:
                nonlocal_ans[0] = min(nonlocal_ans[0], d)
                if nei not in visited:
                    dfs(nei)

        nonlocal_ans = [ans]
        dfs(1)

        return nonlocal_ans[0]