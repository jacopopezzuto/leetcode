class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stop_to_buses = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(i)

        queue=deque([(source,0)])
        visited_stops = set([source])
        visited_buses=set()
        while queue:
            current_stop, buses_taken = queue.popleft()
            for bus in stop_to_buses[current_stop]:
                if bus in visited_buses:
                    continue
                visited_buses.add(bus)
                for stop in routes[bus]:
                    if stop==target:
                        return buses_taken+1
                    if stop not in visited_stops:
                        visited_stops.add(stop)
                        queue.append((stop,buses_taken+1))
        return -1