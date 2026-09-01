from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_count = max(counts.values())
        num_max = 0
        for task in counts.values():
            if task == max_count:
                num_max += 1
        formula = (max_count - 1) * (n + 1) + num_max
        return max(formula, len(tasks))


        