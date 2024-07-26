# Problem: Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        
        m_heap=[]
        for cnt in freq.values():
            m_heap.append(-cnt)
        
        wait_queue=deque()
        heapq.heapify(m_heap)
        time=0
        
        while m_heap or wait_queue:
            time+=1
            
            if m_heap:
                cnt_freq=heapq.heappop(m_heap)+1
                if cnt_freq:
                    wait_queue.append((time+n,cnt_freq))
            
            if wait_queue and wait_queue[0][0]==time:
                heapq.heappush(m_heap,wait_queue.popleft()[1])
        
        return time


