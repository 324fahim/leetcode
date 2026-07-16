class SummaryRanges(object):

    def __init__(self):
        self.nums = set()

    def addNum(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.nums.add(value)

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        if not self.nums:
            return []

        arr = sorted(self.nums)
        res = []

        start = arr[0]
        end = arr[0]

        for x in arr[1:]:
            if x == end + 1:
                end = x
            else:
                res.append([start, end])
                start = end = x

        res.append([start, end])
        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()