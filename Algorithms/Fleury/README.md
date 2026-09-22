# Fleury’s Algorithm — Euler

## Algorithm Explanation
Fleury’s Algorithm is an O(V·E) or O(E²) constructive algorithm that finds an Eulerian circuit in an undirected graph by progressively walking along unused edges while maintaining graph integrity.

Instead of relying on recursive backtrack stacks (like Hierholzer's) or local cycle decompositions (like Tucker's), it operates through four direct steps:
1. **Eulerian Feasibility & Degree Verification:** Check that every vertex has an even degree (deg(v) mod 2 = 0) and that all vertices with edges belong to the connected component of crossing 1.
2. **Candidate Edge Evaluation:** At current crossing u, identify all incident streets that have not yet been traversed.
3. **Bridge Detection (Fleury's Rule):** Before traversing an edge, verify whether removing it will disconnect the remaining unused graph. Never traverse a **bridge** unless it is the only remaining street out of crossing u. ("Never burn a bridge unless forced to.")
4. **Traversal & Edge Deletion:** Traverse the selected non-bridge street, mark it as used (burned), and advance to the neighboring crossing. Repeat this step until all M streets are visited and the circuit terminates back at crossing 1.

---

## Prerequisites to Run the Code
* **Python:** Python 3.8+ (tested on Python 3.12).
* **Dependencies:** None (Pure Python standard library: `sys`, `collections`, `argparse`, `time`, `random`).

---

## Instructions to Run the Code
Sample cases based on [https://cses.fi/problemset/task/1691](https://cses.fi/problemset/task/1691)

### A. Run with Sample Input File
Execute Fleury's algorithm on the provided sample input file (`input_sample.txt`):
```bash
python fluery.py --file input_sample.txt
```

### B. Run Complete Automated Benchmark Suite
Runs Fleury's algorithm against dynamic failure adaptation scenarios and boundary checks:
```bash
python fluery.py --file input_sample.txt --suite
```

### C. Simulate Specific Edge or Node Failures
```bash
# Simulate failure due to an odd degree vertex (e.g., node 3 degree imbalance):
python fluery.py --file input_sample.txt --fail-odd 3

# Simulate failure due to a disconnected graph component:
python fluery.py --file input_sample.txt --fail-disconnected

# Simulate failure due to starting node isolation (Post Office / Node 1 disconnected):
python fluery.py --file input_sample.txt --fail-isolate-1
```

### D. Enter Custom Graph Interactively
```bash
python fluery.py --input
# Enter n and m on line 1, followed by m edges "u v" (one per line). Press Enter when finished.
```

### E. Generate and Test Random Connected Graph
```bash
python fluery.py --random 8
```

---

## Result of Sample Run
Sample cases based on [https://cses.fi/problemset/task/1691](https://cses.fi/problemset/task/1691)

<img width="1517" height="813" alt="image" src="https://github.com/user-attachments/assets/f9a3f317-eb0c-4d68-9b55-b019894f2902" />


### Baseline Run Output (Verbatim Terminal Output)
```text
Executed command: python fluery.py --file input_sample.txt
====================================================================================================
LOADED GRAPH FROM FILE (6 Crossings, 8 Streets) — START NODE: 1
====================================================================================================
Phase 1: Eulerian Feasibility & Degree Verification
----------------------------------------------------------------------------------------------------
* Crossing 1: degree = 2 (Even [OK])
* Crossing 2: degree = 4 (Even [OK])
* Crossing 3: degree = 4 (Even [OK])
* Crossing 4: degree = 2 (Even [OK])
* Crossing 5: degree = 2 (Even [OK])
* Crossing 6: degree = 2 (Even [OK])
-> Eulerian circuit existence confirmed: all vertices have even degrees and form a single component.

Phase 2: Step-by-Step Fleury Traversal & Bridge Evaluations
----------------------------------------------------------------------------------------------------
Step   Crossing   Candidate Edges           Bridge Evaluation                        Chosen Edge     Remaining 
----------------------------------------------------------------------------------------------------
1      1          e1(1-2), e2(1-3)          e1: Non-Bridge (Safe)                    e1 (1 -> 2)     7         
2      2          e3(2-3), e4(2-4), e5(2-6) e3: Non-Bridge (Safe)                    e3 (2 -> 3)     6         
3      3          e2(1-3), e6(3-5), e7(3-6) e2: BRIDGE! [Avoided]                    e6 (3 -> 5)     5         
4      5          e8(4-5)                   Only 1 option left [Forced bridge]       e8 (5 -> 4)     4         
5      4          e4(2-4)                   Only 1 option left [Forced bridge]       e4 (4 -> 2)     3         
6      2          e5(2-6)                   Only 1 option left [Forced bridge]       e5 (2 -> 6)     2         
7      6          e7(3-6)                   Only 1 option left [Forced bridge]       e7 (6 -> 3)     1         
8      3          e2(1-3)                   Only 1 option left [Forced bridge]       e2 (3 -> 1)     0         
----------------------------------------------------------------------------------------------------
Circuit closed successfully at Post Office (Crossing 1).

Phase 3: Final Circuit Traversal Walk
----------------------------------------------------------------------------------------------------
Starting at Post Office (Crossing 1):
1 -(e1)-> 2 -(e3)-> 3 -(e6)-> 5 -(e8)-> 4 -(e4)-> 2 -(e5)-> 6 -(e7)-> 3 -(e2)-> 1
----------------------------------------------------------------------------------------------------
Eulerian Circuit Output: 1 2 3 5 4 2 6 3 1
Execution Time: 0.0013 seconds
```

> **Note on the trace format:** Unlike Tucker's or Hierholzer's algorithms which decompose graphs into sub-cycles or use backtracking recursion, Fleury's Algorithm performs direct forward walk with explicit reachability tests. At **Step 3**, notice that edge `e2(1-3)` leads straight back to the starting post office 1. A naive greedy traversal would traverse `e2(1-3)` and prematurely terminate at node 1 with degree 0, permanently stranding the outer crossings `4, 5, 6`. Fleury's bridge test flags `e2(1-3)` as a bridge of the remaining graph, avoids it, and safely crosses non-bridge edge `e6(3-5)`.

---

## AI Tools Usage Disclosure
In compliance with Institut Teknologi Sepuluh Nopember academic honesty guidelines for group coursework:
* **AI Model / Assistant Used:** Claude
* **Scope of AI Assistance:**
  * Assisted in structuring and implementing Fleury's algorithm in `fluery.py`.
  * Formatted the step-by-step execution trace, command-line arguments (`--suite`, `--fail-odd`, etc.), and verbatim report logs to match the group's signature documentation format.
* **Verification & Ownership:** All source code, algorithm traces, and mathematical explanations have been reviewed, verified, and tested by the group members.
