# Problem: Online Election - https://leetcode.com/problems/online-election/

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []
        count = {}
        leader = -1
        max_votes = 0
        for person in persons:
            count[person] = count.get(person, 0) + 1
            if count[person] >= max_votes:
                leader = person
                max_votes = count[person]
            self.leaders.append(leader)

    def q(self, t: int) -> int:
        index = bisect_right(self.times, t)
        return self.leaders[index - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)