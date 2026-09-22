# Tucker's Algorithm — Euler

## Prerequisites to Run the Code

- **Python**: Python 3.8+ (tested on Python 3.12).
- **Dependencies**: **None** (Pure Python standard library: `sys`, `collections`, `argparse`, `random`).

---

## Instructions to Run the Code

### A. Run with Sample Input File
Execute Tyler's algorithm on the provided sample input file (`input_sample.txt`):
```bash
python tucker.py --file input_sample.txt
```

### B. Run Complete Automated Benchmark Suite
Runs Tucker's algorithm against dynamic failure adaptation scenarios and boundary checks:
```bash
python tucker.py --file input_sample.txt --suite
```

### C. Simulate Specific Edge or Node Failures
```bash
# Simulate failure due to an odd degree vertex (e.g., node 3 degree imbalance):
python tucker.py --file input_sample.txt --fail-odd 3

# Simulate failure due to a disconnected graph component:
python tucker.py --file input_sample.txt --fail-disconnected

# Simulate failure due to starting node isolation (Post Office / Node 1 disconnected):
python tucker.py --file input_sample.txt --fail-isolate-1
```

### D. Enter Custom Graph Interactively
```bash
python tucker.py --input
# Enter n and m on line 1, followed by m edges "u v" (one per line). Press Enter when finished.
```

### E. Generate and Test Random Connected Graph
```bash
python tucker.py --random 8
```

---

## Result of Sample Run

### Baseline Run Output (Verbatim Terminal Output)
Executed command: `python tucker.py --file input_sample.txt`

```text
Executed command: python tucker.py --file input_sample.txt
====================================================================================================
LOADED GRAPH FROM FILE (6 Crossings, 8 Streets) — START NODE: 1
====================================================================================================
Phase 1: Arbitrary Local Edge Pairing
----------------------------------------------------------------------------------------------------
  * Crossing 1: Paired e1(1-2) <-> e2(1-3)
  * Crossing 2: Paired e1(1-2) <-> e3(2-3)  |  Paired e4(2-4) <-> e5(2-6)
  * Crossing 3: Paired e2(1-3) <-> e3(2-3)  |  Paired e6(3-5) <-> e7(3-6)
  * Crossing 4: Paired e4(2-4) <-> e8(4-5)
  * Crossing 5: Paired e6(3-5) <-> e8(4-5)
  * Crossing 6: Paired e5(2-6) <-> e7(3-6)

Phase 2: Disjoint Sub-Cycle Decomposition
----------------------------------------------------------------------------------------------------
  * Cycle 0 (Component 0): e1(1-2) -> e3(2-3) -> e2(3-1)
    [Sub-tour Path: 1 -> 2 -> 3 -> 1]
  * Cycle 1 (Component 1): e4(2-4) -> e8(4-5) -> e6(5-3) -> e7(3-6) -> e5(6-2)
    [Sub-tour Path: 2 -> 4 -> 5 -> 3 -> 6 -> 2]

Phase 3: Cycle Merging via Local Pairing Swaps
----------------------------------------------------------------------------------------------------
Step  Crossing  Intersecting Cycles  Swap Operation performed                            Status
----------------------------------------------------------------------------------------------------
1     2         Cycle 0 & Cycle 1    Old Pairs: (e1-e3), (e4-e5)                         [+] MERGED
                                     New Pairs: (e1-e5), (e4-e3)
                                     -> Cycle 0 and Cycle 1 joined into unified component.

Phase 4: Final Circuit Traversal Walk
----------------------------------------------------------------------------------------------------
Starting at Post Office (Crossing 1):
  1 -(e1)-> 2 -(e5)-> 6 -(e7)-> 3 -(e6)-> 5 -(e8)-> 4 -(e4)-> 2 -(e3)-> 3 -(e2)-> 1
----------------------------------------------------------------------------------------------------
Eulerian Circuit Output: 1 2 6 3 5 4 2 3 1
Execution Time: 0.0006 seconds
```

**Note on the trace format:** Unlike Fleury's Algorithm, Tucker's Algorithm does not perform expensive global bridge checks (O(E^2)). Instead, it operates entirely via local edge pairings, decomposing the graph into initial 2-regular sub-cycles and iteratively performing local edge-swaps at shared vertices. This reduces total execution time to O(V+E) linear time, making it fully optimal for CSES Task 1691 constraints (M ≤ 200,000).

---

## AI Tools Usage Disclosure

In compliance with Institut Teknologi Sepuluh Nopember academic honesty guidelines for group coursework:
- **AI Model / Assistant Used**: Google Gemini
- **Scope of AI Assistance**:
  1. Assisted in writing the python program for Tucker's algorithm.
  2. Formatted step-by-step execution traces and adaptation reports to match the group's signature report style.
- **Verification & Ownership**: All source code, algorithm traces, and mathematical explanations have been reviewed, verified, and tested by the group members.
