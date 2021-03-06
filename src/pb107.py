"""
Problem 107 of Project Euler.

https://projecteuler.net/problem=107

Kruskal's algorithm.
"""

from lib.datastructs import DisjointSets


def problem107(filename="txt/pb107.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        vertices = f.readlines()
    vertices = [string.split(",") for string in vertices]

    edges = []
    for i, vertex in enumerate(vertices):
        for j in range(i):
            if vertex[j].isdigit():
                edges.append(Edge(int(vertex[j]), i, j))

    # cc = connected_components, mst = minimum_spanning_tree
    cc = DisjointSets(len(vertices))
    mst = set()
    edges.sort(key=lambda e: e.weight)
    for e in edges:
        u, v = e.vertices
        if cc.get_representative(u) != cc.get_representative(v):
            mst = mst.union({e})
            cc.set_union(u, v)
    return sum(e.weight for e in edges) - sum(e.weight for e in mst)


class Edge:
    def __init__(self, weight, u, v):
        self.weight = weight
        self.vertices = (u, v)