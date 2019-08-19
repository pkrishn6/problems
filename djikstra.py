from collections import defaultdict
from heapq import *


class Graph:
    def __init__(self, edges):
        self.graph = defaultdict(list)
        for node, neighbor, cost in edges:
            self.graph[node].append((cost, neighbor))

    def djikstra(self, start, target):
        q = [(0, start, ())]
        mins = {start: 0}

        while q:
            cost, v1, path = heappop(q)
            path = (v1, path)
            if v1 == target:
                return (cost, path)
            for c, v2 in self.graph.get(v1, ()):
                cur_cost = mins.get(v2, None)
                new_cost = cost + c
                if cur_cost is None or new_cost < cur_cost:
                    mins[v2] = new_cost
                    heappush(q, v2, path)



if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

    g = Graph(edges)

    print "=== Dijkstra ==="
    print edges
    print "A -> E:"
    print g.dijkstra( "A", "E")
