class UnionFind:
    def __init__(self, arr):
        self.arr = arr
        self.nodes = set()
        for i, j in arr:
            self.nodes.add(i)
            self.nodes.add(j)
        self.parent = {i: i for i in self.nodes}
        self.rank = {i: 1 for i in self.nodes}

    def find(self, node: int) -> int:
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, node1: int, node2: int) -> bool:
        par1, par2 = self.find(node1), self.find(node2)

        if par1 == par2:
            return False

        if self.rank[par1] >= self.rank[par2]:
            self.parent[par2] = par1
            self.rank[par1] += self.rank[par2]
            self.rank[par2] = 0
        else:
            self.parent[par1] = par2
            self.rank[par2] += self.rank[par1]
            self.rank[par1] = 0
        return True