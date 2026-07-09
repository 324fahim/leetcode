class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        if k == 1:
            return 0

        pairs = []
        n = len(weights)

        for i in range(n - 1):
            pairs.append(weights[i] + weights[i + 1])

        pairs.sort()

        small = sum(pairs[:k - 1])
        large = sum(pairs[-(k - 1):])

        return large - small