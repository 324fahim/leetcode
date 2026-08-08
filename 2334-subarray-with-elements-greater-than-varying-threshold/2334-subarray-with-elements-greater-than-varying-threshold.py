class Solution(object):
    def validSubarraySize(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """

        n = len(nums)
        stack = []

        for i in range(n + 1):
            # Sentinel value at the end
            curr = 0 if i == n else nums[i]

            while stack and nums[stack[-1]] >= curr:
                idx = stack.pop()

                # Left boundary is stack[-1] + 1
                left = stack[-1] + 1 if stack else 0

                # Right boundary is i - 1
                length = i - left

                # nums[idx] is the minimum of this range
                if nums[idx] * length > threshold:
                    return length

            stack.append(i)

        return -1