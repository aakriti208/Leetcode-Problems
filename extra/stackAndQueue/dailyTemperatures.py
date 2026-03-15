class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        stack = []
        res = [0] * n
        for i in range(n):
           # current temp is warmer than whatever is on top → answer those indices
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                # days to wait = distance between indices
                res[j] = i - j
            stack.append(i)
        # remaining indices in stack stay 0 (never warmer)
        return res

        