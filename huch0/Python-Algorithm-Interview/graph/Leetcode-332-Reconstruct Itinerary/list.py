class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from_to_map = collections.defaultdict(list)
        route = []

        for a, b in sorted(tickets):
            from_to_map[a].append(b)

        def dfs(departure):
            # Traverse all of departure's possible arrivals
            while from_to_map[departure]:
                dfs(from_to_map[departure].pop(0))

            # if there is no remain arrivals from departure
            # it's the last arrival between remaining airports.
            route.append(departure)

        dfs("JFK")

        # Route stored airports from end to start.
        # Reverse the route
        return route[::-1]
