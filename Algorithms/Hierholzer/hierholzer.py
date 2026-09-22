import sys

def main():
    tokens = []
    def next_token():
        nonlocal tokens
        while not tokens:
            line = sys.stdin.readline()
            if not line:
                return None
            tokens = line.split()
            tokens.reverse()
        return tokens.pop()

    t_n = next_token()
    if t_n is None:
        return
    n = int(t_n)
    m = int(next_token())

    deg = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]

    for i in range(m):
        u = int(next_token())
        v = int(next_token())
        deg[u] += 1
        deg[v] += 1
        adj[u].append((v, i))
        adj[v].append((u, i))

    # Parity check: all vertices must have even degree, node 1 must have edges
    for i in range(1, n + 1):
        if deg[i] & 1:
            sys.stdout.write("IMPOSSIBLE\n")
            sys.stdout.flush()
            return
    if deg[1] == 0:
        sys.stdout.write("IMPOSSIBLE\n")
        sys.stdout.flush()
        return

    # Iterative Hierholzer's Algorithm using a stack
    used = [False] * m
    stack = [1]
    path = []

    while stack:
        u = stack[-1]

        # Pop edges that have already been traversed from the other direction
        while adj[u] and used[adj[u][-1][1]]:
            adj[u].pop()

        if adj[u]:
            v, eid = adj[u].pop()
            used[eid] = True
            stack.append(v)
        else:
            path.append(stack.pop())

    # If graph has disconnected components with edges, circuit won't visit all edges
    if len(path) != m + 1:
        sys.stdout.write("IMPOSSIBLE\n")
        sys.stdout.flush()
        return

    # Output route (path is collected in reverse)
    path.reverse()
    sys.stdout.write(" ".join(map(str, path)) + "\n")
    sys.stdout.flush()

if __name__ == '__main__':
    main()
