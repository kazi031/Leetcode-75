class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(set)

        for bus, route in enumerate(routes):
            for stop in route:
                graph[stop].add(bus)

        ans = 0

        queue = collections.deque([source])
        seen_stop = set()
        seen_route = set()

        seen_stop.add(source)

        while queue:
            for i in range(len(queue)):
                stop = queue.popleft()

                if stop == target:
                    return ans
                
                for routeID in graph[stop]:
                    if routeID not in seen_route:
                        for stops in routes[routeID]:
                            if stops not in seen_stop:
                                queue.append(stops)
                                seen_stop.add(stops)
                        seen_route.add(routeID)
            ans += 1
        
        return -1