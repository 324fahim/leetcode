class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefixGcd = []

        mx = 0
        for x in nums:
            if x > mx:
                mx = x
            prefixGcd.append(self.gcd(x, mx))

        prefixGcd.sort()

        ans = 0
        l, r = 0, len(prefixGcd) - 1

        while l < r:
            ans += self.gcd(prefixGcd[l], prefixGcd[r])
            l += 1
            r -= 1

        return ans