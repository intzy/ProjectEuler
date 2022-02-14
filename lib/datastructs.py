class DisjointSets:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1 for _ in range(size)]

    def get_representative(self, n):
        if self.parent[n] == n:
            return n

        parent = self.get_representative(self.parent[n])
        self.parent[n] = parent
        return parent

    def set_union(self, n, m):
        n = self.get_representative(n)
        m = self.get_representative(m)
        if n == m:
            return
        if self.size[n] < self.size[m]:
            n, m = m, n
        self.parent[m] = n
        self.size[n] += self.size[m]

    def set_size(self, n):
        rep = self.get_representative(n)
        return self.size[rep]
