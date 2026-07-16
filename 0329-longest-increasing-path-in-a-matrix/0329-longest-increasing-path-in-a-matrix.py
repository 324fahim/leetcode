class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]

            best = 1

            for dx, dy in dirs:
                x = i + dx
                y = j + dy

                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    best = max(best, 1 + dfs(x, y))

            dp[i][j] = best
            return best

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))

        return ans