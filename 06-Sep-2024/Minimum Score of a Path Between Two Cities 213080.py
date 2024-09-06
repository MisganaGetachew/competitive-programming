# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj=[[] for _ in range(n+1)]
        for i,j,d in roads:
            adj[i].append((d,j))
            adj[j].append((d,i))
        st=[1]
        visited=[0]*(n+1)
        visited[1]=1
        mn=float("infinity")
        while st:
            x=st.pop(0)
            for dt,i in adj[x]:
                # print(dt,i)
                if visited[i]==0:
                    # print(dt)
                    st.append(i)
                    visited[i]=1
                mn=min(mn,dt)
        return mn
