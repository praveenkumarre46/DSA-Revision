from collections import defaultdict
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist=[[float("inf") for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dist[i][i]=0
        for u,v,wt in edges:
            dist[u][v]=wt
            dist[v][u]=wt
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j]=min(dist[i][j],dist[i][via]+dist[via][j])

        print(dist)
        count=distanceThreshold+1
        finalct=-1
        for i in range(n):
            ct=0
            for j in range(n):
                if i!=j and dist[i][j]<=distanceThreshold:
                    ct+=1
            if ct<=count:
                count=ct
                finalct=i
        return finalct