class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n <= 2:
            return [i for i in range(n)]

        # adjacency list
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            # remove the curr leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                neighbor = neighbors[leaf].pop()
                # remove the only edge left
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        # the remaining nodes are the centroids of the graph
        return leaves
