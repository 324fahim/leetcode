import heapq

class MedianFinder(object):

    def __init__(self):
        self.small = []   # max heap (store negatives)
        self.large = []   # min heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.small, -num)

        # Move largest from small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Keep small having at least as many elements as large
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        return (-self.small[0] + self.large[0]) / 2.0