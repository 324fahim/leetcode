class Solution(object):
    def smallestSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        last = [-1] * 32
        ans = [1] * n

        for i in range(n - 1, -1, -1):
            for b in range(32):
                if (nums[i] >> b) & 1:
                    last[b] = i

            farthest = i
            for b in range(32):
                if last[b] != -1:
                    farthest = max(farthest, last[b])

            ans[i] = farthest - i + 1

        return ans