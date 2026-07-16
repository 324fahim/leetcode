class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rank = {}
        r = 1

        for x in sorted(set(arr)):
            rank[x] = r
            r += 1

        return [rank[x] for x in arr]