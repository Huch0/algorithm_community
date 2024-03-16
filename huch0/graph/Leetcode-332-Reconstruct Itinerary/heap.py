class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(departure: str):
            arrivals = from_to_map[departure]

            while len(arrivals) > 0:
                dfs(heappop(arrivals))

            itinerary.append(departure)

        from_to_map = collections.defaultdict(list)
        itinerary = []

        for ticket in tickets:
            heappush(from_to_map[ticket[0]], (ticket[1]))

        dfs("JFK")

        return itinerary[::-1]
