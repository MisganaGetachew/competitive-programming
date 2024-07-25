# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
            tasks = [(enqueueTime, processingTime, index) for index, (enqueueTime, processingTime) in enumerate(tasks)]
            tasks.sort()
            
            result = []
            heap = []
            time = 0
            i = 0
            n = len(tasks)
            
            while i < n or heap:
                while i < n and tasks[i][0] <= time:
                    heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                    i += 1
                
                if heap:
                    processingTime, index = heapq.heappop(heap)
                    time += processingTime
                    result.append(index)
                else:
                    time = tasks[i][0]
            
            return result      