class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        corners = set()

        minX = float('inf')
        minY = float('inf')
        maxX = float('-inf')
        maxY = float('-inf')

        area = 0

        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)

            minX = min(minX, x1)
            minY = min(minY, y1)
            maxX = max(maxX, x2)
            maxY = max(maxY, y2)

            pts = [
                (x1, y1),
                (x1, y2),
                (x2, y1),
                (x2, y2)
            ]

            for p in pts:
                if p in corners:
                    corners.remove(p)
                else:
                    corners.add(p)

        if area != (maxX - minX) * (maxY - minY):
            return False

        expected = {
            (minX, minY),
            (minX, maxY),
            (maxX, minY),
            (maxX, maxY)
        }

        return corners == expected