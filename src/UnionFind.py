# This class is used to implement the Union-Find (Disjoint Set Union) data structure
class UnionFind:
    # Initialize the UnionFind data structure with a list of tuples representing edges
    def __init__(self, arr):
        self.arr = arr
        self.nodes = set()
        for i, j in arr:
            self.nodes.add(i)
            self.nodes.add(j)
        
        # Initialize parent dictionary, where each node is its own parent initially
        self.parent = {i: i for i in self.nodes}
        
        # Initialize rank dictionary to track the size of each disjoint set
        self.rank = {i: 1 for i in self.nodes}

    # Find the root (representative) of the set to which the given node belongs
    def find(self, node: int) -> int:
        while node != self.parent[node]:
            # Apply path compression to optimize future find operations
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    # Merges the sets to which node1 and node2 belong, if they are not already in the same set
    def union(self, node1: int, node2: int) -> bool:
        par1, par2 = self.find(node1), self.find(node2)

        if par1 == par2:
            # If node1 and node2 were already in the same set, no union is performed
            return False

        if self.rank[par1] >= self.rank[par2]:
            # If the rank of par1 is greater, make par1 the parent of par2 and update the rank of par1
            self.parent[par2] = par1
            self.rank[par1] += self.rank[par2]
            self.rank[par2] = 0
        else:
            # If the rank of par2 is greater, make par2 the parent of par1 and update the rank of par2
            self.parent[par1] = par2
            self.rank[par2] += self.rank[par1]
            self.rank[par1] = 0
        return True