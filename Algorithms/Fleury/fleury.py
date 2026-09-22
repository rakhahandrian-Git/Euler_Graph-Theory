import sys
 
 
def solve():
    # Fast I/O: read all tokens
    input_data = sys.stdin.read().split()
    if not input_data:
        return
 
    n = int(input_data[0])
    m = int(input_data[1])
 
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
 
    idx = 2
    for eid in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].append((v, eid))
        adj[v].append((u, eid))
        deg[u] += 1
        deg[v] += 1
 
    # 1. Feasibility Check: every vertex must have EVEN degree
    for i in range(1, n + 1):
        if deg[i] % 2 != 0:
            sys.stdout.write("IMPOSSIBLE\n")
            return
 
    used_edge = [False] * m
    stack = [1]
    route = []
 
    # 2. Hierholzer's Algorithm: O(N + M)
    while stack:
        u = stack[-1]
 
        # Pop any edges that have already been used
        while adj[u] and used_edge[adj[u][-1][1]]:
            adj[u].pop()
 
        if adj[u]:
            v, eid = adj[u].pop()
            used_edge[eid] = True
            stack.append(v)
        else:
            route.append(stack.pop())
 
    # 3. Check if all m edges were traversed
    if len(route) != m + 1:
        sys.stdout.write("IMPOSSIBLE\n")
    else:
        # Route was collected in post-order, reverse to get the circuit
        sys.stdout.write(" ".join(map(str, route[::-1])) + "\n")
 
 
if __name__ == "__main__":
    solve()
