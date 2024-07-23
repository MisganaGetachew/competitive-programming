# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        cnt = 0
        while maxDoubles > 0 and target > 1:
            if target % 2 == 0:
                target = target/2
                cnt += 1
                maxDoubles -= 1
            else:
                target -= 1
                cnt += 1
        if target > 1:
            return int(cnt + target - 1)
        return int(cnt)

        