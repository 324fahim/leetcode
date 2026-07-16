class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slopes = {}
            duplicate = 1

            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 == x2 and y1 == y2:
                    duplicate += 1
                    continue

                dx = x2 - x1
                dy = y2 - y1

                g = self.gcd(dx, dy)
                dx //= g
                dy //= g

                # Normalize sign
                if dx < 0:
                    dx = -dx
                    dy = -dy
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1

                key = (dy, dx)
                slopes[key] = slopes.get(key, 0) + 1

            best = duplicate
            for cnt in slopes.values():
                best = max(best, cnt + duplicate)

            ans = max(ans, best)

        return ans