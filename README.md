# Minimum Cost Spanning Tree

**Uses Kruskal's algorithm to find the minimum cost spanning tree of a graph.**

Given a .in file representing an undirected graph, find the total sum of edges for the minimum spanning tree (MST). The .in file may also specify edges that must be included in the MST.

A .in file contains graph information in the following order:
1. Number of vertices
1. Number of edges
1. Edges - Starting vertex, ending vertex, and edge weight
1. Number of specified edges for MST
1. Specified eges

## Example

<img align="right" src="https://github.com/bbat2575/Minimum-Cost-Spanning-Tree/blob/main/graphs/graph8-2.png" style="width: 40%;">

For *graph8.in*:

8 &emsp;&emsp;&emsp;&emsp;&emsp; <- Number of vertices  
15 &emsp;&emsp;&emsp;&emsp;&emsp; <- Number of edges  
0 1 0.732 &emsp;&ensp; <- Egdes  
0 3 0.134 &emsp;&ensp; ...  
0 4 0.112 &emsp;&ensp; ...  
1 4 0.770 &emsp;&ensp; ...  
2 5 0.379 &emsp;&ensp; ...  
2 6 0.984 &emsp;&ensp; ...  
2 7 0.577 &emsp;&ensp; ...  
3 4 0.642 &emsp;&ensp; ...  
3 6 0.763 &emsp;&ensp; ...  
3 7 0.589 &emsp;&ensp; ...  
4 5 0.473 &emsp;&ensp; ...  
4 7 0.334 &emsp;&ensp; ...  
5 6 0.748 &emsp;&ensp; ...  
5 7 0.544 &emsp;&ensp; ...  
6 7 0.474 &emsp;&ensp; ...  
4 &emsp;&emsp;&emsp;&emsp;&emsp; <- Number of specified edges for MST  
0 1 &emsp;&emsp;&emsp;&emsp;&nbsp; <- Specified edges  
3 6 &emsp;&emsp;&emsp;&emsp;&nbsp; ...  
2 6 &emsp;&emsp;&emsp;&emsp;&nbsp; ...  
2 5 &emsp;&emsp;&emsp;&emsp;&nbsp; ...  

Output:

```bash
3.44
```

## How To Run

Execute the run script.

```bash
./run.sh
```

NOTE: Ensure execution privileges are available.

```bash
chmod +x run.sh
```

## Testing

Execute the testing script.

```bash
./test.sh
```