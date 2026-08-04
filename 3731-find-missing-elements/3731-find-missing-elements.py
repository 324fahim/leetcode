class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lo = min(nums)
        hi = max(nums)

        s = set(nums)
        ans = []

        for x in range(lo, hi + 1):
            if x not in s:
                ans.append(x)

        return ans