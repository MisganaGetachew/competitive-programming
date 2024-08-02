# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.small = []
        self.larg = []
    def addNum(self, num: int) -> None:
        heappush(self.small, -num)
        heappush(self.larg, -heappop(self.small))
        
        if len(self.larg) > len(self.small):
            heappush(self.small, -heappop(self.larg))

    def findMedian(self) -> float:
        if len(self.small) == len(self.larg):
            return (-self.small[0] + self.larg[0]) / 2.0
        elif len(self.small) > len(self.larg):
            return -self.small[0]
        return self.larg[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()