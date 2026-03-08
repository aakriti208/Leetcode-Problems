from unionFind import UnionFind

def validGraphTree(n, edges):
    uf = UnionFind()
    for u, v in edges:
        if not uf.union(u,v):
            return False
    
    return uf.components == 1