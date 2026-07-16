class Solution(object):
    def isSelfCrossing(self, distance):
        """
        :type distance: List[int]
        :rtype: bool
        """
        n = len(distance)

        for i in range(3, n):
            # Case 1: Current line crosses the line 3 steps ahead
            if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
                return True

            # Case 2: Current line overlaps the line 4 steps ahead
            if i >= 4:
                if (distance[i - 1] == distance[i - 3] and
                    distance[i] + distance[i - 4] >= distance[i - 2]):
                    return True

            # Case 3: Current line crosses the line 5 steps ahead
            if i >= 5:
                if (distance[i - 2] >= distance[i - 4] and
                    distance[i] + distance[i - 4] >= distance[i - 2] and
                    distance[i - 1] <= distance[i - 3] and
                    distance[i - 1] + distance[i - 5] >= distance[i - 3]):
                    return True

        return False