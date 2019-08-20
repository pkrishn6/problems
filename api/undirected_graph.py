from collections import defaultdict
class Graph:
    def __init__(self, edges):
        self.g = defaultdict(list)
        self.seen = []
        for node, neighbor, _ in edges:
            self.g[node].append(neighbor)
            self.g[neighbor].append(node)
            self.vertices.append(node)

    def dfs(self, node, parent):
        if node not in self.g:
            raise KeyError

        self.seen.append(node)
        for neighbor in self.g[node]:
            if neighbor == parent:
                continue
            if neighbor in self.seen:
                return False
            if not self.dfs(neighbor, node):
                return False
        return True


    def hasCycle(self):
        i = 0
        node = None
        for key in self.g.keys():
            if i > 0:
                break
            node = key
            i += 1

        if not self.dfs(node, None):
            return True

        return False

    def bfsCycle(self):
        i = 0
        q = []
        seen = []
        parent = [None for _ in range(len(self.g))]
        for node in self.g.keys():
            if i > 0:
                break
            i += 1
            q.append(node)

        while(q):
            vertex = q.pop(0)
            for cost, n in self.g[vertex]:
                if not seen[n]:
                    seen[n] = True
                    parent[n] = vertex
                    q.append(n)
                elif parent[vertex] != n:
                    return True
        return False


if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("B", "C", 8),
        ("B", "D", 9),
        ("C", "E", 5),
    ]

    g = Graph(edges)
    print(g.hasCycle())
