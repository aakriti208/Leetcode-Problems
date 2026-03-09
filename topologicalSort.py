# Kahn's Algorithm

from collections import deque

def topSort(n, edges):
  # Build adjacency list and in-degree array
  D = defaultdict(list)
  in_degree = [0]*n

  for u, v in edges:
    D[u].append(v)
    in_degree[v] += 1

  # add all nodes with zero dependancy to the Queue
  q = dequeue([i for i in range(n) if in_degree[i] == 0])
  topo_order = []

  # Process the queue
  while q:
    u = q.popleft()
    topo_order.append(u)
    for v in D[u]:
      # 'u' is finished so 'v' has one less prerequisite
      in_degree[v] -= 1
      if in_degree[v] == 0:
        q.append(v)
  
  # Final cycle check
  if len(topo_order) == n:
    return topo_order
  else:
    return []   # Cycle detected!
