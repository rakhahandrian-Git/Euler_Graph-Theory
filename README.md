# Informatics ITS Graph Theory IUP 
## Group 1 Assignment 3

<div align=center>

|    NRP     |           Nama              |
| :--------: |       :------------:        |
| 5025251012 | Khumaidy Syafiq El Maududy  |
| 5025251015 | Renato Kiran Arisandi       |
| 5025251016 | Keven John Gondowardojo     |
| 5025251010 | Agile Octa Agrakha Handrian |

</div>

## Algorithm Explanation

### Euler Path and Euler Circuit

An Euler path is a path in a graph that visits every edge exactly once. An Euler circuit is an Euler path that starts and ends at the same vertex.

For an undirected graph:

- An **Euler circuit** exists if every vertex has an even degree.
- An **Euler path** exists if exactly two vertices have odd degrees.
- If more than two vertices have odd degrees, there is no Euler path or Euler circuit.

### Fleury's Algorithm

Fleury's algorithm is an algorithm used to find an Euler path or Euler circuit in a graph. It works by choosing edges one by one while avoiding bridges whenever there is another available edge.

__Steps__

1. Start from an appropriate vertex.
2. Select an unused edge connected to the current vertex.
3. Avoid choosing a bridge if there is another available edge.
4. Remove the selected edge and move to the next vertex.
5. Repeat until all edges have been used.

### Hierholzer's Algorithm

Hierholzer's algorithm is an algorithm used to find an Euler path or Euler circuit. It works by creating a cycle and then finding additional cycles from vertices that still have unused edges.

__Steps__

1. Start from a suitable vertex and follow unused edges until returning to the starting vertex.
2. Check whether there are still unused edges.
3. If unused edges remain, choose a vertex in the current circuit that has unused edges.
4. Create another circuit from that vertex using unused edges.
5. Merge the new circuit with the existing circuit.
6. Repeat until all edges have been used.

### Tucker's Algorithm

Tucker's algorithm is an algorithm used to find an Euler path or Euler circuit by constructing a sequence of vertices while ensuring that each edge is used exactly once.

__Steps__

1. Start from a suitable vertex.
2. Choose an unused edge connected to the current vertex.
3. Move to the next vertex and mark the edge as used.
4. Continue selecting unused edges while maintaining the Euler path conditions.
5. Repeat until every edge has been used.
6. The resulting sequence of vertices represents the Euler path or Euler circuit.

## Extras
### PDF Reports: https://docs.google.com/document/d/1-2w2EMhnmUNjq3F3008iwsd6wK5erb4S_Uz3BmBnUeM/edit?usp=sharing

## AI Prompt used
<img width="400" height="320" alt="image" src="https://github.com/user-attachments/assets/5b82d528-7e1a-45cd-b5ba-45a69a16b250" />

    AI was (mostly) used to generate the step by step visualizations and verify the steps; given the input and steps

    so from the code, what is the time and space complexity for the fleury and hierholzer code

    create the visualization for each step of the graph


