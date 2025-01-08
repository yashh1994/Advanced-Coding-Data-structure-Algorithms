import heapq
from typing import List, Tuple

def dijkstra(adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
    n = len(adj)  
    dis = [float("inf")] * n 
    dis[src] = 0  

    heap = [(0, src)]
    
    while heap:
        cur_dis, node = heapq.heappop(heap)  # Get node with smallest distance
        
        if cur_dis > dis[node]:
            continue
        
        for nei, weight in adj[node]:
            new_dis = cur_dis + weight
            if new_dis < dis[nei]:
                dis[nei] = new_dis
                heapq.heappush(heap, (new_dis, nei))    
    return dis


if __name__ == "__main__":
    adj = [
        [(1, 4), (2, 1)], 
        [(3, 1)],         
        [(1, 2), (3, 5)], 
        []                
    ]
    
    src = 0  
    distances = dijkstra(adj, src)
    print(f"Shortest distances from node {src}: {distances}")