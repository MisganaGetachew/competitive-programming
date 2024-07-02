# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        def children(lock):
                ans = []
                for i in range(4):
                    dig = str((int(lock[i]) + 1)%10)
                    ans.append(lock[:i] + dig + lock[i+1:])
                    dig = str((int(lock[i]) - 1)%10)
                    ans.append(lock[:i] + dig + lock[i+1:])
                return ans


        q = deque()
        q.append(["0000", 0])
        visited = set(deadends)
        while q:
            node, step = q.popleft()
            if node == target:
                return step
            for ch in children(node):
                if ch not in visited:
                    q.append((ch, step + 1))
                    visited.add(ch)
        return -1 