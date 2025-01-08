"""
Kosaraju's Algorithm for finding Strongly Connected Components (SCC) in a directed graph.

Key Points:
1. **Graph Representation**: Uses adjacency lists.
2. **Two-Pass Algorithm**:
    - **First Pass**: DFS on the original graph to compute finishing times.
    - **Second Pass**: DFS on the transpose graph in decreasing order of finishing times.
3. **Transpose Graph**: Reverse the direction of all edges.
4. **DFS Utilization**: Determines the order of vertices.
5. **Component Identification**: Each DFS tree in the transpose graph is an SCC.
6. **Time Complexity**: O(V + E), where V is vertices and E is edges.
7. **Applications**: Used in social network analysis, compiler optimization, etc.
"""


"""
Take the DFS of the graph
reverse all the edges
Do the DFS of the reversed graph in the order of decreasing finishing times
number of times we call DFS is number of scc.
"""

def dfs(node, visited, stk, mat):
    visited[node] = True
    for nei in mat[node]:
        if not visited[nei]:
            dfs(nei, visited, stk, mat)

    stk.append(node)
def number_of_scc(mat):
    visited = [False] * (len(mat) + 1)
    stk = []
    for n in mat:
        if not visited[n]:
            dfs(n, visited, stk, mat)

    transpose_mat = {i: set() for i in mat}
    for node in mat:
        for nei in mat[node]:
            transpose_mat[nei].add(node)
    visited = [False] * (len(mat) + 1)
    ans = 0
    while stk:
        node = stk.pop()
        if not visited[node]:
            dfs(node, visited, [], transpose_mat)
            ans += 1
    print("SCC is: ",ans)



mat = {1: [2], 2: [3], 3: [1]}
mat = {k: set(v) for k, v in mat.items()}
number_of_scc(mat)