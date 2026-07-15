class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        robot.sort()
        factory.sort()

        n = len(robot)
        m = len(factory)
        INF = 10 ** 18
        memo = {}

        def dfs(i, j):
            if i == n:
                return 0
            if j == m:
                return INF

            if (i, j) in memo:
                return memo[(i, j)]

            # Skip current factory
            ans = dfs(i, j + 1)

            pos, limit = factory[j]
            cost = 0

            # Assign next k robots to current factory
            for k in range(1, min(limit, n - i) + 1):
                cost += abs(robot[i + k - 1] - pos)
                ans = min(ans, cost + dfs(i + k, j + 1))

            memo[(i, j)] = ans
            return ans

        return dfs(0, 0)