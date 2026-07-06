class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        prefixes = [0] * (n + 1)
        cur = 0
        for i in range(n):
            cur += 1 if nums[i] == target else -1
            prefixes[i + 1] = cur

        # Coordinate compression
        sorted_unique = sorted(set(prefixes))
        rank = {v: i + 1 for i, v in enumerate(sorted_unique)}  # 1-indexed for BIT
        m = len(sorted_unique)

        tree = [0] * (m + 1)

        def update(i):
            while i <= m:
                tree[i] += 1
                i += i & (-i)

        def query(i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & (-i)
            return s

        ans = 0
        for p in prefixes:
            r = rank[p]
            ans += query(r - 1)  # count of earlier prefixes strictly less than p
            update(r)

        return ans