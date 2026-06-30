from collections import Counter

class Solution(object):
    def recoverArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums) // 2

        for i in range(1, len(nums)):
            diff = nums[i] - nums[0]
            if diff <= 0 or diff % 2:
                continue

            k = diff // 2
            cnt = Counter(nums)
            ans = []
            ok = True

            for x in nums:
                if cnt[x] == 0:
                    continue
                if cnt[x + 2 * k] == 0:
                    ok = False
                    break
                cnt[x] -= 1
                cnt[x + 2 * k] -= 1
                ans.append(x + k)

            if ok and len(ans) == n:
                return ans