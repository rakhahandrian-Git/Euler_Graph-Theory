# Fleury’s Algorithm — Euler

## Algorithm Explanation

Fleury’s Algorithm is a classical, constructive algorithm that finds an Eulerian circuit in an undirected graph by progressively walking along unused edges while maintaining graph integrity.

Unlike recursive stack methods (like Hierholzer's) or local edge-swapping methods (like Tucker's), Fleury’s algorithm builds the circuit through a direct, greedy traversal governed by one fundamental rule: "Never burn a bridge unless forced to."

It works through four key phases:

### Feasibility & Connectivity Verification

Check that all vertices have an even degree (`deg(v) (mod 2) = 0`).

Verify that all vertices with degree `> 0` belong to the single connected component containing the starting post office (vertex 1).

### Candidate Edge Selection

At current vertex `u`, examine all incident edges that have not yet been traversed.

### Bridge Detection (Fleury's Rule)

If an edge is a bridge of the remaining (unused-edge) subgraph, it must not be chosen unless it is the only candidate left incident to `u`.

A bridge test is conducted via reachability count (BFS/DFS): an edge `e = (u,v)` is a bridge if removing it strictly decreases the number of reachable vertices from `u`.

### Traversal & Edge Deletion

Traverse the selected non-bridge edge to reach the next vertex, mark the edge as used (deleted), and repeat until all `M` edges have been traversed and the route returns to vertex 1.

## Prerequisites to Run the Code

**Python:** Python 3.8+ (tested on Python 3.12).

**Dependencies:** None (Pure Python standard library: sys, collections, argparse, time).

## Instructions to Run the Code

Sample cases based on CSES Task 1691: Mail Delivery.

### A. Run with Sample Input File

Execute Fleury's algorithm on the provided sample input file (`input_sample.txt`):

```bash
python fleury.py --file input_sample.txt
