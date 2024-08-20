# Problem: Smallest Number in Infinite Set - https://leetcode.com/problems/smallest-number-in-infinite-set/description/

class SmallestInfiniteSet:

    def __init__(self):
        self.nums = set()

    def popSmallest(self) -> int:
        smallest = 1
        while smallest in self.nums:
            smallest += 1
        self.nums.add(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num in self.nums:
            self.nums.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)