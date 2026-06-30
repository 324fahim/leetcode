class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        ans = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                mx = 0
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        mx = max(mx, grid[r][c])
                ans[i][j] = mx

        return ans