# Recursively traces through roots list to find the root of a given node's subtree
def find_root(roots, node):
    if roots[int(node)] != node:
        return find_root(roots, roots[int(node)])
    
    # If root found, return it
    return node


# Read in the number of vertices (n) and edges (m)
n = int(input())
m = int(input())

# Read the edges from stdin.
edges = []
for _ in range(m):
    edges.append(input().split())

# Read the A edges. You may want to use a different data-structure.
n_A, A = int(input()), []

for _ in range(n_A):
	A.append(input().split())

mst_weight = 0

# Create a roots list to keep track of nodes with a common lineage (used for detecting cycles)
roots = [i for i in range(n)]

# Sort the edges by weight (ascending order)
edges = sorted(edges, key = lambda x: x[2])

# Add the connected edges from A
for a in A:
    # Retrieve vertexes of an edge from A
    v1, v2 = a
    
    # Find the roots of v1 and v2
    root1 = find_root(roots, v1)
    root2 = find_root(roots, v2)
    
    # Reflect the joining of these nodes by joining their subtrees (make one root for both subtrees)
    roots[root1] = root2
    
    # Add the edge to the final result
    for e in edges:
        if ((e[0], e[1]) == (v1, v2)) or ((e[0], e[1]) == (v2, v1)):
            mst_weight += float(e[2])

# Use Kruskal's algorithm to complete the tree
for e in edges:
    # Retrieve vertexes and weight of an edge from edges
    v1, v2, weight = e
    
    # If adding this edge doesn't produce a cycle (i.e. v1 and v2 don't have same root), then add it
    if find_root(roots, int(v1)) != find_root(roots, int(v2)):
        # Find the roots of v1 and v2
        root1 = find_root(roots, v1)
        root2 = find_root(roots, v2)
        
        # Reflect the joining of these nodes by joining their subtrees
        roots[root1] = root2  
        
        # Add the edge to the final result
        mst_weight += float(weight)

# Print the weight of the mst to two decimal-places. 
print('{:.2f}'.format(mst_weight))

# References:
# [1] “Kruskal’s Minimum Spanning Tree (MST) Algorithm” GeeksforGeeks. Accessed: May, 1, 2024. [Online] 
#     Available: https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
