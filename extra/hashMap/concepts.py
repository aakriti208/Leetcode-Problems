from collections import Counter, defaultdict

seen = set()                # this is for membership
count = Counter(nums)       # this is for counting; {value:frequency} , missing keys --> 0
groups = defaultdict(list)  # this is or grouping; missing keys --> []
hashMap = {}                # value --> index; stores as a key:value pair

count[x] += 1                   # safe even if x absent (Counter/defaultdict)
count.get(x, 0)                 # safe read on a plain dict
groups[key].append(x)           # safe append (defaultdict)



count[x] += 1
count.get(x, 0)
groups[key].append(x)

