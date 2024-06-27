# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        unlocked = set([0])
        que = deque([0])

        while que:
            node = que.popleft()
            for el in rooms[node]:
                if el not in unlocked:
                    unlocked.add(el)
                    que.append(el)
        return len(unlocked) == len(rooms)
