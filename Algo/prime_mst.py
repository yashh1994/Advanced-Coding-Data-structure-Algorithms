import heapq
from typing import List

def spanningTree(V: int, adj: List[List[int]]) -> int:
    mst_weight = 0
    visited = [False] * V  
    min_heap = [(0, 0)]  

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        
        if visited[u]:
            continue
        
        visited[u] = True
        mst_weight += weight
        

        for v, w in adj[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
    
    return mst_weight

graph = [
    [(1, 2), (3, 6)],
    [(0, 2), (2, 3), (3, 8), (4, 5)],
    [(1, 3), (4, 7)],
    [(0, 6), (1, 8)],
    [(1, 5), (2, 7)]
]

V = len(graph)
wei = spanningTree(V,graph)
print("Minimum Spanning Tree: ",wei)
