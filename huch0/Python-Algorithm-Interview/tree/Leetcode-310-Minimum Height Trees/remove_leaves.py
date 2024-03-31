class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Only one node exists
        if n == 1:
            return [0]

        tree = collections.defaultdict(list)

        # Construct a tree
        for e in edges:
            tree[e[0]].append(e[1])
            tree[e[1]].append(e[0])

        # Leaves to iterate
        leaves = []

        for i in range(n + 1):
            if len(tree[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)

            new_leaves = []

            for leaf in leaves:
                # Remove edges incident from leaves
                adjacent = tree[leaf].pop()
                tree[adjacent].remove(leaf)

                # Add new leaves
                if len(tree[adjacent]) == 1:
                    new_leaves.append(adjacent)

            # Iterate new leaves
            leaves = new_leaves

        return leaves
