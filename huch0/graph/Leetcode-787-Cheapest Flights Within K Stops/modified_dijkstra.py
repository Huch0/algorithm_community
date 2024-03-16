class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)

        # Construct graph
        for u, v, w in flights:
            graph[u].append((v, w))

        # for store 'best' way to 'node' with k 'steps'
        # default value is infinity
        best = collections.defaultdict(lambda: float('inf'))

        # for store which node should be traced in next iteration.
        cheapest_next_traverse = [(0, -1, src)]  # price, steps, node

        while cheapest_next_traverse:
            price, steps, node = heapq.heappop(cheapest_next_traverse)

            # Do not need to traverse over k steps
            # price > best[(steps, node)] means that
            # already best way to node with specific steps is already found
            if steps > k or price > best[(steps, node)]:
                continue

            # It means cheapest price is found
            # because this code traverse graph with lowest price
            if node == dst:
                return price

            for v, w in graph[node]:
                new_price = price + w

                # It means cheaper price to specific (steps, node) is found.
                if new_price < best[(steps + 1, v)]:
                    # Always Move to cheapest way
                    heapq.heappush(cheapest_next_traverse,
                                   (new_price, steps + 1, v))
                    # Update Best way to v node with steps
                    best[(steps + 1, v)] = new_price

        # Can't find dst until steps exceeds k
        # There is no route.
        return -1
