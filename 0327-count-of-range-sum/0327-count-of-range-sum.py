class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        prefix = [0]
        s = 0
        for num in nums:
            s += num
            prefix.append(s)

        def sort(lo, hi):
            if hi - lo <= 1:
                return 0

            mid = (lo + hi) // 2
            count = sort(lo, mid) + sort(mid, hi)

            j = k = mid
            temp = []
            r = mid

            for left in prefix[lo:mid]:
                while k < hi and prefix[k] - left < lower:
                    k += 1
                while j < hi and prefix[j] - left <= upper:
                    j += 1
                count += j - k

                while r < hi and prefix[r] < left:
                    temp.append(prefix[r])
                    r += 1
                temp.append(left)

            temp.extend(prefix[r:hi])
            prefix[lo:hi] = temp

            return count

        return sort(0, len(prefix))