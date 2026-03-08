from unionFind import UnionFind

def numberOfComponents(n, edges):
    uf = UnionFind()
    
    for u, v in edges:
        uf.union(u, v)
    return uf.components
         