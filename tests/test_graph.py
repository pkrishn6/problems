from unittest.mock import patch
from api import graph
import time

def test_djikstra():
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

    g = graph.Graph(edges)
    print(g)
    print(edges)
    print("A -> E:")
    print(g.djikstra("A", "E"))

def test_topo():
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

    def _mock(*args):
        time.sleep(1)
        return ["Z", "A"]

    with patch('api.graph.Graph.topoSort', _mock):
        g = graph.Graph(edges)
        result = g.topoSort("A")
        print(result)
        assert("Z" in result)
