class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.components = n
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def Union(self, a, b):
        rootA = self.parent[a]
        rootB = self.parent[b]
        
        if rootA == rootB: return False
        
        if self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        elif self.rank[rootB] > self.rank[rootA]:
            self.parent[rootA] = rootB
        else:
            self.rootB = rootA
            self.rank[rootA] += 1
        
        self.components -= 1
        return True

