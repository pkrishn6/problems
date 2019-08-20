from collections import defaultdict
from heapq import *

class Graph:
    def __init__(self, edges):
        self.graph = defaultdict(list)
        for node, neighbor, cost in edges:
            self.graph[node].append((cost, neighbor))

    def djikstra(self, start, target):
        mins = {start: 0}
        q = [(0, start, ())]
        seen = set()
        while q:
            cost, v1, path = heappop(q)
            if v1 in seen:
                continue

            path = (v1, path)
            if v1 == target:
                return v1, path

            for c, v2 in self.graph[v1]:
                if v2 in seen:
                    continue
                new_cost = cost + c
                cur_cost = mins.get(v2, None)
                if cur_cost is None or new_cost < cur_cost:
                    mins[v2] = new_cost
                    heappush(q, (new_cost, v2, path))

        return float('inf')

    def hasCycle(self):
        indegree = defaultdict(int)
        q = []
        for vertex, neighbors in self.graph.items():
            for cost, neighbor in neighbors:
                indegree[neighbor] += 1

        for vertex, _ in self.graph.items():
            if not indegree[vertex]:
                q.append(vertex)
        count = 0
        print(indegree)
        while(q):
            element = q.pop(0)
            for cost, neighbor in self.graph[element]:
                indegree[neighbor] -= 1
                if not indegree[neighbor]:
                    q.append(neighbor)
            count += 1
        if count == len(self.graph):
            return False
        return True

    def topoSort(self, start=None):
        WHITE, GRAY, BLACK = 0, 1, 2
        colors = defaultdict(int)
        topo_stack = []

        def dfs(node):
            colors[node] = GRAY
            for _, neighbor in self.graph[node]:
                if colors[neighbor] == GRAY:
                    return False
                elif colors[neighbor] == BLACK:
                    continue
                elif not dfs(neighbor):
                    return False
            colors[node] = BLACK
            topo_stack.append(node)
            return True

        if start:
            if not dfs(start):
                return []
            return topo_stack

        for node in self.graph.keys():
            print("Topo of node", node)
            if colors[node] == WHITE:
                if not dfs(node):
                    return []

        return topo_stack


if __name__ == "__main__":
    test2 = [
        ("A", "B", 1),
        ("B", "A", 1)
    ]

    test3 = [
        ("A", "B", 1),
        ("B", "C", 1),
        ("B", "D", 1),
        ("C", "E", 1),
        ("C", "F", 1),
        ("G", "H", 1),
        ("H", "I", 1),
        ("I", "J", 1)
    ]

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

    g = Graph(test3)
    print(g.graph)

    print("A -> E:")
    # print(g.djikstra( "A", "E"))
    print(g.topoSort())
    print(g.hasCycle())
