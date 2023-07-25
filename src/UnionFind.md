# UnionFind Module

UnionFind Module is a Python module that provides an efficient implementation of the Union-Find (Disjoint Set Union) data structure.

## Class

### `UnionFind`

The `UnionFind` class is a data structure that represents disjoint sets. It provides the following methods:

1. `__init__(self, arr: List[Tuple[int, int]])`
   - Initializes the UnionFind data structure with a list of tuples representing edges.
   - The input `arr` is a list of tuples, where each tuple represents an edge between two nodes.
   - Time Complexity: O(n)
   - Space Complexity: O(n)

2. `find(self, node: int) -> int`
   - Finds the root (representative) of the set to which the given `node` belongs.
   - Utilizes path compression for optimization.
   - Time Complexity: O(log(n)) (approximately, due to path compression)
   - Space Complexity: O(1)

3. `union(self, node1: int, node2: int) -> int`
   - Merges the sets to which `node1` and `node2` belong, if they are not already in the same set.
   - Uses union by rank for optimization to maintain a balanced tree.
   - Returns 1 if a union is performed, 0 if `node1` and `node2` were already in the same set.
   - Time Complexity: O(log(n)) (approximately, due to union by rank)
   - Space Complexity: O(1)

## Usage

1. Import the `dsakit` from pip using:

```python
pip install dsakit
```

2. Import class/functions from UnionFind as needed:

```python
from UnionFind import *
```

## Example

1. Create an instance of the UnionFind class and initialize it with a list of vertices:

```python
vertices = [1,2,3,4,5]
uf = UnionFind(vertices)
```

2. Use the union method to join the vertices on the basis of edges:

```python
edges = [(1, 2), (2, 3), (4, 5)]
for v1, v2 in edges:
    uf.union(edges)
```

3. Find the number of disjoint group of vertices with the help of find method (better way will be to count the non-zero elements in rank):

```python
disjoint_groups = set()
for i in uf.parent:
    disjoint_groups.add(uf.find(i))
print(len(disjoint_groups))
```