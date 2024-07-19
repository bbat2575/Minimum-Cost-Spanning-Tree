# Minimum Cost Spanning Tree

**Uses Kruskal's algorithm to find the minimum cost spanning tree of a graph.**

Given a .in file representing an undirected graph, find the total sum of edges for the minimum spanning tree.

A .in file contains graph information in the following order:
1. Number of vertices
1. Number of edges
1. Edges - Starting vertex, ending vertex, and edge weight (edge weight is ignored!)
1. Number of queries
1. Queries

## Example

For *graph8.in*:

8 &emsp;&emsp;&emsp;&emsp;&emsp; <- Number of vertices  
7 &emsp;&emsp;&emsp;&emsp;&emsp; <- Number of edges  
0 1 0.802 &emsp;&ensp; <- Egdes  
0 5 0.937 &emsp;&ensp; ...  
0 7 0.019 &emsp;&ensp; ...  
1 5 0.233 &emsp;&ensp; ...  
2 3 0.154 &emsp;&ensp; ...  
3 4 0.651 &emsp;&ensp; ...  
6 7 0.010 &emsp;&ensp; ...  
8 &emsp;&emsp;&emsp;&emsp;&emsp; <- Number of queries  
2 3 &emsp;&emsp;&emsp;&emsp;&nbsp; <- Queries  
5 2 &emsp;&emsp;&emsp;&emsp;&nbsp; ...  
2 1 &emsp;&emsp;&emsp;&emsp;&nbsp; ...  
2 4 &emsp;&emsp;&emsp;&emsp;&nbsp; ...  
7 0 &emsp;&emsp;&emsp;&emsp;&nbsp; ...  
7 1 &emsp;&emsp;&emsp;&emsp;&nbsp; ...  
1 4 &emsp;&emsp;&emsp;&emsp;&nbsp; ...  
5 7 &emsp;&emsp;&emsp;&emsp;&nbsp; ...  

<p align="center">
    <img src="https://github.com/bbat2575/PathFinder/blob/main/graphs/graph8.png"/>
</p>

Output:

```bash
2, 3 -> Path Exists!
5, 2 -> No Path Exists.
2, 1 -> No Path Exists.
2, 4 -> Path Exists!
7, 0 -> Path Exists!
7, 1 -> Path Exists!
1, 4 -> No Path Exists.
5, 7 -> Path Exists!
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