class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = n * (n + 1) // 2
        root = int(total ** 0.5)

        if root * root == total:
            return root
        return -1