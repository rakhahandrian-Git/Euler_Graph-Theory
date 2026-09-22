import sys

def token_stream():
    for line in sys.stdin:
        for token in line.split():
            yield token

def solve():
    tokens = token_stream()
    
    first_token = next(tokens, None)
    if first_token is None:
        return
    
    n = int(first_token)  # Number of crossings
    m = int(next(tokens)) # Number of streets
    
    edges = []
    incident = [[] for _ in range(n + 1)]
    
    # Reads exactly M edges and stops expecting input immediately
    for e_id in range(m):
        u = int(next(tokens))
        v = int(next(tokens))
        edges.append((u, v))
        incident[u].append(e_id)
        incident[v].append(e_id)
        
    # Every vertex must have an EVEN degree 
    for v in range(1, n + 1):
        if len(incident[v]) % 2 != 0:
            print("IMPOSSIBLE")
            return
            
    # Crossing 1 (Post Office) must have connected streets 
    if len(incident[1]) == 0:
        print("IMPOSSIBLE")
        return

    def get_other_endpoint(e_id, v):
        u, w = edges[e_id]
        return w if u == v else u

    # Step 1: Arbitrary Local Edge Pairing at Each Vertex
    transition = {}
    for v in range(1, n + 1):
        e_list = incident[v]
        for i in range(0, len(e_list), 2):
            e1, e2 = e_list[i], e_list[i + 1]
            transition[(e1, v)] = e2
            transition[(e2, v)] = e1

    # Step 2: Decompose Graph into Disjoint Closed Sub-Cycles
    edge_to_cycle = [-1] * m
    num_cycles = 0
    total_visited_edges = 0
    
    for start_e in range(m):
        if edge_to_cycle[start_e] != -1:
            continue
            
        curr_e = start_e
        curr_v = edges[curr_e][0]
        
        while edge_to_cycle[curr_e] == -1:
            edge_to_cycle[curr_e] = num_cycles
            total_visited_edges += 1
            curr_v = get_other_endpoint(curr_e, curr_v)
            curr_e = transition[(curr_e, curr_v)]
            
        num_cycles += 1

    # Disjoint Set Union (DSU) for cycle merging
    parent = list(range(num_cycles))
    
    def find(i):
        path = []
        while parent[i] != i:
            path.append(i)
            i = parent[i]
        for node in path:
            parent[node] = i
        return i

    def union(i, j):
        root_i, root_j = find(i), find(j)
        if root_i != root_j:
            parent[root_i] = root_j

    # Step 3: Tucker Cycle Merging via Local Swaps
    for v in range(1, n + 1):
        e_list = incident[v]
        if len(e_list) <= 2:
            continue
        
        base_e = e_list[0]
        for i in range(2, len(e_list), 2):
            curr_e = e_list[i]
            c1 = find(edge_to_cycle[base_e])
            c2 = find(edge_to_cycle[curr_e])
            
            if c1 != c2:
                p1 = transition[(base_e, v)]
                p2 = transition[(curr_e, v)]
                
                # Perform local swap at vertex v
                transition[(base_e, v)] = p2
                transition[(p2, v)] = base_e
                
                transition[(curr_e, v)] = p1
                transition[(p1, v)] = curr_e
                
                union(c1, c2)

    # Check Graph Connectivity
    active_components = set(find(edge_to_cycle[e]) for e in range(m))
    if len(active_components) > 1 or total_visited_edges < m:
        print("IMPOSSIBLE")
        return

    # Final Traversal Starting at Crossing 1 (Post Office)
    curr_e = incident[1][0]
    curr_v = 1
    circuit = [1]
    
    for _ in range(m):
        curr_v = get_other_endpoint(curr_e, curr_v)
        circuit.append(curr_v)
        curr_e = transition[(curr_e, curr_v)]
        
    if circuit[-1] != 1 or len(circuit) != m + 1:
        print("IMPOSSIBLE")
        return

    # Print the resulting circuit
    print(*(circuit))

if __name__ == '__main__':
    solve()
