class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def check(num):
            x = num

            while x > 0:
                d = x % 10
                if d == 0 or num % d != 0:
                    return False
                x //= 10

            return True

        ans = []

        for num in range(left, right + 1):
            if check(num):
                ans.append(num)

        return ans