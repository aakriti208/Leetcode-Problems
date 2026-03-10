from collections import defaultdict, deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        D = defaultdict(list)
        in_degree = [0]*numCourses
        for u, v in prerequisites:
            D[u].append(v)
            in_degree[v] += 1

        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed = 0

        while q:
            node = q.popleft()
            completed += 1
            for neighbor in D[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        return completed == numCourses
        