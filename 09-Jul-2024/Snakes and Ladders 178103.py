# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def helper(s):
            r = (s - 1) // n
            c = (s - 1) % n
            if r % 2 == 0:
                return n - 1 - r, c
            else:
                return n - 1 - r, n - 1 - c
              

        q = deque()
        q.append([1, 0])
        visited = set()
        while q:
            square, step = q.popleft()
            if square == n * n:
                return step
            for new in range(square + 1, min(square + 6, n * n) + 1):
                r, c = helper(new)
                if board[r][c] != -1:
                    new = board[r][c]
                if new not in visited:
                    visited.add(new)
                    q.append((new, step + 1))
        return - 1
