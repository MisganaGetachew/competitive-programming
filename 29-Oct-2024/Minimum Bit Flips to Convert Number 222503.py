# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution(object):
    def minBitFlips(self, start, goal):
        return bin(start ^ goal).count('1')   