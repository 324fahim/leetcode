class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = set()
        prev = set()

        for num in arr:
            curr = {num}
            for x in prev:
                curr.add(x | num)
            prev = curr
            res |= curr

        return len(res)