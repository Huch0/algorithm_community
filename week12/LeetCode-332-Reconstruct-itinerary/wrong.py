class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        sorted_tickets = sorted(tickets)
        dept, arrive = [], []
        route = []
        cur_dept = "JFK"
        cur_arrive = ""
        for i in range(len(sorted_tickets)):
            dept.append(sorted_tickets[i][0])
            arrive.append(sorted_tickets[i][1])
        route.append(cur_dept)

        for _ in range(len(sorted_tickets)):
            if cur_dept in dept:
                cur_index = dept.index(cur_dept)
                cur_arrive = arrive[cur_index]
                route.append(cur_arrive)
                dept[cur_index] = '\0'
                arrive[cur_index] = '\0'
                cur_dept = cur_arrive
            else:
                continue

        return route
