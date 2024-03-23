class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        win = {}
        los = {}
        
        for i in range(len(matches)):
            if matches[i][0] in win:
                win[matches[i][0]] += 1 
            else:
                win[matches[i][0]] = 1 
        
        for i in range(len(matches)):
            if matches[i][1] in los:
                los[matches[i][1]] += 1 
            else:
                los[matches[i][1]] = 1 
        
        won = []
        lost = []
        for i in win:
            if i not in los:
                won.append(i)
        
        for i in los:
            if los[i] == 1:
                lost.append(i)  
        
        return [sorted(won), sorted(lost)]
                       