class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k % 2 == 0 or k % 5 == 0:
            return -1

        rem = 0
        seen = set()

        length = 0

        while rem not in seen:
            seen.add(rem)
            rem = (rem * 10 + 1) % k
            length += 1

            if rem == 0:
                return length

        return -1