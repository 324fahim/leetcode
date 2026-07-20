class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        total = m * n

        k %= total

        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                idx = i * n + j
                new_idx = (idx + k) % total

                x = new_idx // n
                y = new_idx % n

                ans[x][y] = grid[i][j]

        return ans