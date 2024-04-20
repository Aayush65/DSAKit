class UnionFind:
    # Initialize the UnionFind data structure with a list of tuples representing edges
    def __init__(self, nodes):
        self.__nodes = nodes
        
        # Initialize parent dictionary, where each node is its own parent initially
        self.__parent = {i: i for i in self.__nodes}

        # Initialize rank dictionary to track the size of each disjoint set
        self.__rank = {i: 1 for i in self.__nodes}

    @property
    def Parent(self):
        return self.__parent
    
    @property
    def Rank(self):
        return self.__rank
    
    # Find the root (representative) of the set to which the given node belongs
    def find(self, node: int) -> int:
        while node != self.__parent[node]:
            # Apply path compression to optimize future find operations
            self.__parent[node] = self.__parent[self.__parent[node]]
            node = self.__parent[node]
        return node

    # Merges the sets to which node1 and node2 belong, if they are not already in the same set
    def union(self, node1: int, node2: int) -> bool:
        par1, par2 = self.find(node1), self.find(node2)

        if par1 == par2:
            # If node1 and node2 were already in the same set, no union is performed
            return False

        if self.__rank[par1] >= self.__rank[par2]:
            # If the rank of par1 is greater, make par1 the parent of par2 and update the rank of par1
            self.__parent[par2] = par1
            self.__rank[par1] += self.__rank[par2]
            self.__rank[par2] = 0
        else:
            # If the rank of par2 is greater, make par2 the parent of par1 and update the rank of par2
            self.__parent[par1] = par2
            self.__rank[par2] += self.__rank[par1]
            self.__rank[par1] = 0
        return True