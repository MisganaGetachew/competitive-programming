# Problem: Reorganize String - https://leetcode.com/problems/reorganize-string/description/

class Solution:
    from collections import Counter 
    import heapq
    def reorganizeString(self, s: str) -> str:
            cnt = Counter(s)
            ans = []
            prev_cnt, prev_char = 0, "" 
            mx_heap = [(-freq, char) for char, freq in cnt.items()]
            heapq.heapify(mx_heap)
            while mx_heap:
                cnt, char = heapq.heappop(mx_heap)
                ans.append(char)
                if prev_cnt < 0:
                    heapq.heappush(mx_heap, (prev_cnt, prev_char))
                prev_cnt = cnt + 1
                prev_char = char
                
            if len(ans) == len(s):
                return "".join(ans)
            else:
                return ""