import { useState } from "react";

const sections = [
  { id: "arrays", label: "Arrays", icon: "▤", color: "#f97316" },
  { id: "strings", label: "Strings", icon: "≋", color: "#22d3ee" },
  { id: "hashmaps", label: "Hashmaps", icon: "⊞", color: "#a3e635" },
  { id: "defaultdict", label: "Defaultdict", icon: "⊟", color: "#e879f9" },
  { id: "tradeoffs", label: "Array vs Map vs Set", icon: "⚖", color: "#fbbf24" },
  { id: "loops", label: "Loops", icon: "↺", color: "#34d399" },
  { id: "returning", label: "Returning Values", icon: "↩", color: "#f472b6" },
  { id: "prefix", label: "Prefix Sums", icon: "∑", color: "#818cf8" },
  { id: "micro", label: "Micro-Techniques", icon: "⚡", color: "#fb923c" },
  { id: "templates", label: "Templates", icon: "⬡", color: "#2dd4bf" },
];

const content = {
  arrays: {
    color: "#f97316",
    intro: "Arrays are the backbone of 80% of LeetCode problems. Master every manipulation.",
    subsections: [
      {
        title: "Accessing & Updating Elements",
        body: `arr = [10, 20, 30, 40, 50]
arr[0]     # → 10  (first)
arr[-1]    # → 50  (last)
arr[-2]    # → 40  (second to last)

# Update — O(1)
arr[2] = 99   # → [10, 20, 99, 40, 50]

# Safe access — guard against out of bounds
if 0 <= i < len(arr):
    val = arr[i]`,
        complexity: [["Access", "O(1)"], ["Update", "O(1)"]],
        mistake: "arr[-1] works in Python but crashes in many other languages. On a whiteboard, don't assume this.",
      },
      {
        title: "In-Place Modifications",
        body: `# Modify without creating new array — O(1) space
def square_inplace(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] ** 2

# Overwrite from two sources in-place (merge sorted)
arr = [1, 2, 3, 0, 0, 0]
# Fill from the BACK to avoid overwriting unread data`,
        complexity: [["In-place modify", "O(n) time, O(1) space"]],
        mistake: "Creating a new array when the problem says in-place wastes O(n) space. Interviewers notice this.",
      },
      {
        title: "Resizing — Append / Insert / Remove",
        body: `arr = [1, 2, 3]

# Append — O(1) amortized
arr.append(4)           # [1, 2, 3, 4]

# Insert at index — O(n)  ← shifts everything right
arr.insert(1, 99)       # [1, 99, 2, 3, 4]

# Remove by value — O(n) — removes first occurrence
arr.remove(99)

# Remove by index — O(n) (shifts left)
arr.pop(1)              # removes index 1
arr.pop()               # removes last — O(1)

# Delete range
del arr[1:3]            # removes indices 1 and 2`,
        complexity: [["append", "O(1) amortized"], ["insert(i)", "O(n)"], ["pop()", "O(1)"], ["pop(i)", "O(n)"], ["remove(v)", "O(n)"]],
        mistake: "insert(0, val) and pop(0) are O(n) — they shift the whole array. Use deque if you need fast front operations.",
      },
      {
        title: "Reversing Arrays",
        body: `arr = [1, 2, 3, 4, 5]

# In-place reverse — O(n) time, O(1) space
arr.reverse()

# New reversed list — O(n) space
rev = arr[::-1]

# Manual two-pointer reverse
l, r = 0, len(arr) - 1
while l < r:
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1`,
        complexity: [["reverse()", "O(n) time, O(1) space"], ["[::-1]", "O(n) time, O(n) space"]],
        mistake: "arr[::-1] creates a NEW list. If the problem says in-place, use .reverse() or the two-pointer method.",
      },
      {
        title: "Swapping Elements",
        body: `# Pythonic swap — no temp variable needed
arr[i], arr[j] = arr[j], arr[i]

# Python evaluates the right side FULLY first, then assigns.
# So no overwrite issue.

# Common use: partition in quicksort
def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1`,
        complexity: [["Swap", "O(1)"]],
        mistake: "In Java/C++ you need a temp variable. Python's tuple unpacking is atomic — right side evaluates first.",
      },
      {
        title: "Iterating Forward vs Backward",
        body: `arr = [1, 2, 3, 4, 5]

# Forward
for i in range(len(arr)):
    print(arr[i])

# Backward — when right-to-left processing matters
for i in range(len(arr)-1, -1, -1):
    print(arr[i])

# Backward by value (no index needed)
for x in reversed(arr):
    print(x)

# When to go backward:
# - Filling array from the end (merge sorted arrays)
# - Avoiding index shift when deleting during iteration
# - Trapping Rain Water / next greater element problems`,
        complexity: [["Either direction", "O(n)"]],
        mistake: "range(len(arr)-1, -1, -1) — the STOP is -1 (exclusive), so index 0 IS included. range(len-1, 0, -1) misses index 0.",
      },
      {
        title: "Two-Pointer Array Manipulation",
        body: `# Pattern 1: Opposite ends (two sum sorted, palindrome)
l, r = 0, len(arr) - 1
while l < r:
    if condition: l += 1
    else: r -= 1

# Pattern 2: Same direction fast/slow (remove duplicates)
slow = 0
for fast in range(len(arr)):
    if arr[fast] != arr[slow]:
        slow += 1
        arr[slow] = arr[fast]
return slow + 1   # new length

# Pattern 3: Two separate arrays (merge)
i, j = 0, 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        result.append(a[i]); i += 1
    else:
        result.append(b[j]); j += 1
result.extend(a[i:]); result.extend(b[j:])`,
        complexity: [["Two pointer", "O(n) time, O(1) space"]],
        mistake: "Use while l < r, not while l <= r. When l == r you're at the same element — no valid pair.",
      },
      {
        title: "Edge Cases to Always Check",
        body: `def solve(arr):
    # 1. Empty array
    if not arr: return []

    # 2. Single element
    if len(arr) == 1: return arr[0]

    # 3. All duplicates: [1,1,1,1]
    # 4. Already sorted: [1,2,3,4]
    # 5. Reverse sorted: [4,3,2,1]
    # 6. Negative numbers: [-3,-1,0,2]
    # 7. Single pair: [a, b]

    # Most two-pointer bugs hide in cases 6 and 7`,
        complexity: [],
        mistake: "Most wrong answers on LeetCode come from not handling empty input or single-element arrays. Check these FIRST.",
      },
    ],
  },

  strings: {
    color: "#22d3ee",
    intro: "Strings in Python are immutable sequences. Every 'modification' creates a new string — know the cost.",
    subsections: [
      {
        title: "Iterating Characters",
        body: `s = "hello"

for c in s:               # by value
    print(c)

for i in range(len(s)):   # by index
    print(s[i])

for i, c in enumerate(s): # both — most common
    print(i, c)

# Character checks
c.isalpha()   # True if letter
c.isdigit()   # True if digit
c.isalnum()   # True if letter or digit
c.lower()     # lowercase
c.upper()     # uppercase`,
        complexity: [["Iterate", "O(n)"], ["s[i] access", "O(1)"]],
        mistake: "Strings are immutable — s[i] = 'x' throws TypeError. Convert to list first.",
      },
      {
        title: "Converting Between Strings and Arrays",
        body: `s = "hello world"

list(s)             # ['h','e','l','l','o',' ','w','o','r','l','d']
s.split()           # ['hello', 'world']  (any whitespace)
s.split(',')        # split on comma

''.join(chars)      # list of chars → string  FAST O(n)
' '.join(words)     # list of words → string

list(map(int, "1 2 3".split()))  # [1, 2, 3]

str(42)             # "42"
ord('a')            # 97  char → ASCII
chr(97)             # 'a' ASCII → char
ord(c) - ord('a')   # 0-25 index for lowercase letters`,
        complexity: [["list(s)", "O(n)"], ["''.join(arr)", "O(n)"]],
        mistake: "s.split() removes empty strings. s.split(' ') keeps them. Know which you need.",
      },
      {
        title: "Building Strings Efficiently",
        body: `# SLOW — O(n²) — each += creates a new string
result = ""
for c in chars:
    result += c       # quadratic!

# FAST — O(n) — collect then join once
parts = []
for c in chars:
    parts.append(c)
result = ''.join(parts)

# One-liner with generator
result = ''.join(c for c in s if c.isalpha())`,
        complexity: [["String concat in loop", "O(n²)"], ["join()", "O(n)"]],
        mistake: "result += char in a loop is the #1 string performance mistake. Always collect in a list and join at the end.",
      },
      {
        title: "String Slicing",
        body: `s = "abcdefgh"

s[2:5]     # "cde"     indices 2,3,4
s[:3]      # "abc"     from start to 2
s[3:]      # "defgh"   from 3 to end
s[::2]     # "aceg"    every 2nd char
s[::-1]    # "hgfedcba" reversed

# Compare substrings
s[i:j] == s[k:l]     # O(length of slice)

# Check prefix/suffix
s.startswith("abc")   # O(k)
s.endswith("xyz")     # O(k)`,
        complexity: [["s[i:j]", "O(k) where k = slice length"], ["startswith/endswith", "O(k)"]],
        mistake: "s[i:j] is O(j-i), not O(1). Many comparisons in a loop compounds this. Consider hashing for O(1) substring comparison.",
      },
      {
        title: "Reversing Strings & Palindromes",
        body: `# Reverse — new string
rev = s[::-1]

# Two-pointer in-place (convert first)
chars = list(s)
l, r = 0, len(chars)-1
while l < r:
    chars[l], chars[r] = chars[r], chars[l]
    l += 1; r -= 1
rev = ''.join(chars)

# Palindrome — simple
s == s[::-1]

# Palindrome — skip non-alnum (LC 125)
def isPalindrome(s):
    s = s.lower()
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum(): l += 1
        while l < r and not s[r].isalnum(): r -= 1
        if s[l] != s[r]: return False
        l += 1; r -= 1
    return True`,
        complexity: [["s[::-1]", "O(n) time + space"], ["Two-pointer", "O(n) time, O(1) space"]],
        mistake: "For palindrome with non-alnum chars, use inner while loops to skip them BEFORE comparing. Don't compare then skip.",
      },
      {
        title: "Sliding Window on Strings",
        body: `# Fixed window — max vowels in window of k
def max_vowels(s, k):
    vowels = set('aeiou')
    count = sum(1 for c in s[:k] if c in vowels)
    res = count
    for i in range(k, len(s)):
        count += (s[i] in vowels)
        count -= (s[i-k] in vowels)
        res = max(res, count)
    return res

# Variable window — longest substring without repeat
def lengthOfLongestSubstring(s):
    seen = {}
    l = res = 0
    for r, c in enumerate(s):
        if c in seen and seen[c] >= l:
            l = seen[c] + 1
        seen[c] = r
        res = max(res, r - l + 1)
    return res`,
        complexity: [["Sliding window", "O(n)"]],
        mistake: "Window size = r - l + 1, not r - l. At l=2, r=4: indices 2,3,4 = 3 elements = 4-2+1.",
      },
      {
        title: "When to Convert to List vs Operate Directly",
        body: `# Operate directly — READING only
def count_vowels(s):
    return sum(1 for c in s if c in 'aeiou')

# Convert to list — need index-based WRITES
def reverse_string(s):
    arr = list(s)            # O(n) extra space
    l, r = 0, len(arr)-1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1; r -= 1
    return ''.join(arr)

# Rule:
# Read only → string directly (no copy)
# Modify by index → convert to list`,
        complexity: [["list(s)", "O(n) extra space"]],
        mistake: "Converting to list just to read wastes O(n) space. Know when you actually need mutability.",
      },
    ],
  },

  hashmaps: {
    color: "#a3e635",
    intro: "Hashmaps reduce O(n²) brute force to O(n) in dozens of patterns. Know every operation cold.",
    subsections: [
      {
        title: "Creating and Updating Maps",
        body: `d = {}

# Set
d['key'] = 'value'
d['count'] = d.get('count', 0) + 1

# Initialize
d = {'a': 1, 'b': 2}
d = dict(zip(keys, values))

# Delete
del d['key']              # KeyError if missing
d.pop('key')              # returns value, KeyError if missing
d.pop('key', None)        # safe — returns None if missing

# Check existence — O(1)
'key' in d
'key' not in d

# Iterate
for k in d:               # keys
for v in d.values():      # values
for k, v in d.items():    # both`,
        complexity: [["get/set", "O(1) avg"], ["delete", "O(1) avg"], ["'k' in d", "O(1)"]],
        mistake: "d['key'] raises KeyError if missing. Use d.get('key') or check 'key' in d first.",
      },
      {
        title: "Counting Frequencies",
        body: `# Manual
freq = {}
for x in nums:
    freq[x] = freq.get(x, 0) + 1

# Counter — cleanest
from collections import Counter
freq = Counter(nums)
freq['a']             # count (0 if missing, no KeyError)
freq.most_common(k)   # top k: [(val, count), ...]

# Counter vs regular dict:
# Counter → missing key returns 0
# Regular dict → missing key raises KeyError`,
        complexity: [["Build", "O(n)"], ["Lookup", "O(1)"]],
        mistake: "Counter returns 0 for missing keys. Regular dict raises KeyError. Choose based on whether 'missing = 0' makes sense.",
      },
      {
        title: ".get() vs Conditional Checks",
        body: `d = {'a': 1}

d.get('b', 0)      # → 0   no KeyError
d.get('a', 0)      # → 1

# Use .get() for counting and default returns
d[x] = d.get(x, 0) + 1

# Use 'in' check when logic branches on existence
if 'key' in d:
    process(d['key'])     # key exists
else:
    initialize()          # key missing, different path

# setdefault — set if missing, return value either way
d.setdefault('key', []).append(val)
# Equivalent but longer:
if 'key' not in d: d['key'] = []
d['key'].append(val)`,
        complexity: [["get()", "O(1)"], ["setdefault()", "O(1)"]],
        mistake: "d.get('key') returns None if missing — not 0, not False. Always specify default: d.get('key', 0).",
      },
      {
        title: "Storing Indices vs Values",
        body: `# Store VALUE — frequency counting
freq = {}
for x in nums:
    freq[x] = freq.get(x, 0) + 1

# Store INDEX — Two Sum, finding pairs
seen = {}
for i, x in enumerate(nums):
    if target - x in seen:
        return [seen[target-x], i]
    seen[x] = i    # store index, not count!

# Store FIRST occurrence
first = {}
for i, x in enumerate(nums):
    if x not in first:
        first[x] = i   # only set once

# Store LIST of indices
positions = {}
for i, x in enumerate(nums):
    positions.setdefault(x, []).append(i)`,
        complexity: [["All patterns", "O(n) build, O(1) lookup"]],
        mistake: "For Two Sum, store the INDEX not the count. Storing the wrong thing is a very common bug.",
      },
      {
        title: "Key Hashmap Patterns",
        body: `# Two Sum
seen = {}
for i, n in enumerate(nums):
    if target - n in seen:
        return [seen[target-n], i]
    seen[n] = i

# Subarray sum = k (prefix + map)
count = prefix = 0
freq = {0: 1}
for n in nums:
    prefix += n
    count += freq.get(prefix - k, 0)
    freq[prefix] = freq.get(prefix, 0) + 1

# Group anagrams (sorted key)
from collections import defaultdict
groups = defaultdict(list)
for word in words:
    groups[tuple(sorted(word))].append(word)

# Longest consecutive sequence
nums_set = set(nums)
res = 0
for n in nums_set:
    if n - 1 not in nums_set:   # start of sequence
        length = 1
        while n + length in nums_set:
            length += 1
        res = max(res, length)`,
        complexity: [["All patterns", "O(n)"]],
        mistake: "Subarray sum = k REQUIRES initializing freq = {0: 1}. Without it, subarrays starting at index 0 are missed.",
      },
    ],
  },

  defaultdict: {
    color: "#e879f9",
    intro: "defaultdict eliminates key-existence boilerplate. Use it when missing keys should auto-initialize.",
    subsections: [
      {
        title: "defaultdict(int) — Counting",
        body: `from collections import defaultdict

# Regular dict — crashes
d = {}
d['a'] += 1    # KeyError!

# defaultdict(int) — missing keys default to 0
d = defaultdict(int)
d['a'] += 1    # works! → {'a': 1}
d['b'] += 5    # → {'b': 5}

# Frequency counting
freq = defaultdict(int)
for c in s:
    freq[c] += 1

# Difference from Counter:
# Counter: initialized from iterable, has most_common()
# defaultdict(int): starts empty, no most_common()`,
        complexity: [["Access/set", "O(1)"]],
        mistake: "defaultdict auto-creates a key with default value when you ACCESS it — even just reading. d['missing'] creates the key. Use d.get() to read safely.",
      },
      {
        title: "defaultdict(list) — Grouping",
        body: `from collections import defaultdict

# Adjacency list (graph)
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)   # no need to check if u exists

# Group anagrams
groups = defaultdict(list)
for word in words:
    key = ''.join(sorted(word))
    groups[key].append(word)

# Weighted adjacency list
adj = defaultdict(list)
for src, dst, weight in flights:
    adj[src].append((dst, weight))`,
        complexity: [["Access/append", "O(1)"]],
        mistake: "defaultdict(list) not defaultdict(list()). Pass the TYPE as factory, not a called instance.",
      },
      {
        title: "defaultdict(set) — Unique Grouping",
        body: `from collections import defaultdict

# Group unique values — no duplicates per key
d = defaultdict(set)
for key, val in pairs:
    d[key].add(val)

# Unique neighbors in graph
neighbors = defaultdict(set)
for u, v in edges:
    neighbors[u].add(v)
    neighbors[v].add(u)

# defaultdict(set) vs defaultdict(list)
# set  → uniqueness + O(1) membership check
# list → order preserved + duplicates allowed`,
        complexity: [["add", "O(1)"], ["'x' in set", "O(1)"]],
        mistake: "Sets are unordered. You can't index into a defaultdict(set). If order matters, use list.",
      },
      {
        title: "When defaultdict Beats Regular dict — and When Not",
        body: `# USE defaultdict when:
# - Missing keys should always initialize the same way
# - Building adjacency lists, frequency maps, groupings
graph = defaultdict(list)    # cleaner than checking 'if u not in graph'

# USE regular dict when:
# - Missing key is MEANINGFUL (signals 'not found')
# - You're checking key existence as part of logic

# Example where regular dict is BETTER:
# Two Sum — absence means complement not seen yet
seen = {}    # NOT defaultdict
for i, n in enumerate(nums):
    if target - n in seen:        # absence is meaningful
        return [seen[target-n], i]
    seen[n] = i

# If seen were defaultdict, seen[target-n] would silently
# create the key with 0 — masking the 'not found' case`,
        complexity: [],
        mistake: "Don't use defaultdict when the ABSENCE of a key carries meaning. It silently creates keys and masks bugs.",
      },
    ],
  },

  tradeoffs: {
    color: "#fbbf24",
    intro: "Choosing the right structure is the difference between O(n) and O(n²). Know the tradeoffs cold.",
    subsections: [
      {
        title: "When to Use Each Structure",
        body: `# ARRAY — when:
arr = [1, 2, 3]
arr[i]         # O(1) — ordered, index-based access
               # Use when: order matters, indices matter,
               # memory is tight, iterating everything

# HASHMAP — when:
d = {key: val}
d[key]         # O(1) — arbitrary key lookup
               # Use when: frequency count, key-value mapping,
               # fast lookup by non-integer key, caching

# SET — when:
s = {1, 2, 3}
x in s         # O(1) — membership only
               # Use when: only need yes/no lookup,
               # deduplication, no value needed`,
        complexity: [["Array index", "O(1)"], ["Dict lookup", "O(1) avg"], ["Set lookup", "O(1) avg"], ["List search", "O(n)"]],
        mistake: "'x in list' inside a loop = O(n²). Convert to set before the loop if doing many membership checks.",
      },
      {
        title: "Lookup Complexity Comparison",
        body: `arr = [3, 1, 4, 1, 5]
3 in arr          # O(n) — linear scan

d = {'a': 1}
'a' in d          # O(1) — hash

s = {1, 2, 3}
3 in s            # O(1) — hash

# Sorted array + binary search
import bisect
arr = sorted([3,1,4,1,5])
pos = bisect.bisect_left(arr, 3)   # O(log n)

# When sorted array + bisect beats hashmap:
# - Range queries: "all elements between x and y"
# - Nearest value: "closest to target"
# - Order matters for output`,
        complexity: [["list 'in'", "O(n)"], ["dict/set 'in'", "O(1) avg"], ["bisect", "O(log n)"]],
        mistake: "The most common O(n²) trap: 'x in list' inside a for loop. Convert the list to set BEFORE the loop.",
      },
      {
        title: "Memory Tradeoffs",
        body: `# List — most compact
arr = [1,2,3,4,5]     # ~120 bytes (5 elements)

# Set — ~4x overhead for hashing
s = {1,2,3,4,5}       # ~216 bytes

# Dict — most memory (key + value + hash)
d = {i:i for i in range(5)}  # ~232 bytes

# For bounded integer keys (0 to n) — use array instead!
# No hash overhead, O(1) access
seen = [False] * n    # O(n) memory, faster than set
seen[i] = True
if seen[j]: ...

# This avoids hash overhead when keys are integers in a range`,
        complexity: [],
        mistake: "For bounded integers (0 to n), a boolean array is faster AND uses less memory than a set. Use it.",
      },
      {
        title: "Real Interview Decision Examples",
        body: `# Two Sum → hashmap {value: index}
# (need lookup by value → dict)

# Contains Duplicate → set
# (just yes/no membership, no value needed → set)

# Valid Anagram → Counter or sort
# (compare character frequencies → Counter)

# Longest Consecutive Sequence → set
# (O(1) membership, no duplicates → set)

# Top K Frequent → Counter + heap OR bucket array
# (frequency map + ordering)

# Subarray Sum = K → prefix + hashmap
# (need fast lookup of prefix sums)

# General rule:
# 'x in ___' inside a loop → make it a set or dict
# Key-value relationship → dict
# Frequency counting → Counter or dict
# Just existence → set`,
        complexity: [],
        mistake: "Sets can't contain mutable objects. To store a list in a set, convert to tuple first: s.add(tuple(lst)).",
      },
    ],
  },

  loops: {
    color: "#34d399",
    intro: "Every LeetCode pattern reduces to one of these loop structures. Master the setup.",
    subsections: [
      {
        title: "Standard For Loop + Enumerate",
        body: `for x in nums:               # value only
    ...

for i in range(len(nums)):   # index only
    ...

for i, x in enumerate(nums): # both — prefer this
    ...

for i, x in enumerate(nums, 1):  # 1-indexed
    ...

for i in range(0, len(nums), 2):  # every other
    ...

for a, b in zip(list1, list2):    # two lists
    ...

for i, (a,b) in enumerate(zip(list1, list2)):
    ...`,
        complexity: [["for loop", "O(n)"]],
        mistake: "Don't use range(len(nums)) when you only need values — use 'for x in nums'. Use range(len) only when you need the index.",
      },
      {
        title: "Reverse Loop",
        body: `# With range — gives index
for i in range(len(arr)-1, -1, -1):
    print(arr[i])

# With reversed() — gives value
for x in reversed(arr):
    print(x)

# When to go backward:
# 1. Fill from back (merge sorted in-place)
i, j, k = m-1, n-1, m+n-1
while i >= 0 and j >= 0:
    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]; i -= 1
    else:
        nums1[k] = nums2[j]; j -= 1
    k -= 1

# 2. Next greater element (monotonic stack)
for i in range(len(temps)-1, -1, -1):
    while stack and temps[stack[-1]] <= temps[i]:
        stack.pop()
    result[i] = stack[-1] - i if stack else 0
    stack.append(i)`,
        complexity: [["Reverse loop", "O(n)"]],
        mistake: "range(len-1, -1, -1) — stop is -1 (exclusive), so index 0 IS included. range(len-1, 0, -1) misses index 0.",
      },
      {
        title: "While Loop Patterns",
        body: `# Two-pointer
l, r = 0, len(arr)-1
while l < r: ...

# Shrink window
while window_invalid and l <= r:
    remove(arr[l]); l += 1

# BFS / stack processing
while queue:
    node = queue.popleft()

# for/else — else runs ONLY if no break occurred
for n in nums:
    if n < 0:
        print("negative found")
        break
else:
    print("all non-negative")   # only if loop completed

# Inner while in outer for — still O(n) if each
# element enters and exits the inner loop at most once
for r in range(n):
    while l < r and invalid:
        l += 1`,
        complexity: [["while loop", "O(n) if pointer advances each iter"]],
        mistake: "Inner while inside for looks like O(n²) but is often O(n) amortized — each element processed at most twice.",
      },
      {
        title: "Two-Pointer Templates",
        body: `# Opposite ends — sorted array, palindrome
l, r = 0, len(arr) - 1
while l < r:
    total = arr[l] + arr[r]
    if total == target: return [l, r]
    elif total < target: l += 1
    else: r -= 1

# Fast/slow same direction — remove element
slow = 0
for fast in range(len(nums)):
    if nums[fast] != val:
        nums[slow] = nums[fast]
        slow += 1
return slow

# Three pointers — Dutch national flag
lo, mid, hi = 0, 0, len(arr)-1
while mid <= hi:
    if arr[mid] == 0:
        arr[lo], arr[mid] = arr[mid], arr[lo]
        lo += 1; mid += 1
    elif arr[mid] == 1:
        mid += 1
    else:
        arr[mid], arr[hi] = arr[hi], arr[mid]
        hi -= 1`,
        complexity: [["Two pointer", "O(n) time, O(1) space"]],
        mistake: "while l < r, not l <= r. l == r means same element — no valid pair to process.",
      },
      {
        title: "Sliding Window Templates",
        body: `# Fixed window
window_val = sum(nums[:k])
result = window_val
for i in range(k, len(nums)):
    window_val += nums[i]
    window_val -= nums[i - k]
    result = max(result, window_val)

# Variable window — maximize
l = result = 0
freq = {}
for r in range(len(s)):
    freq[s[r]] = freq.get(s[r], 0) + 1   # expand right

    while is_invalid(freq):               # shrink left
        freq[s[l]] -= 1
        if freq[s[l]] == 0: del freq[s[l]]
        l += 1

    result = max(result, r - l + 1)      # record after shrink`,
        complexity: [["Sliding window", "O(n)"]],
        mistake: "Record the answer AFTER shrinking. At that point you have the largest valid window ending at r.",
      },
      {
        title: "Nested Loop Optimization",
        body: `# Brute force O(n²) — all pairs
for i in range(n):
    for j in range(i+1, n):
        if arr[i] + arr[j] == target:
            return [i, j]

# → O(n) with hashmap — precompute complement
seen = {}
for i, x in enumerate(arr):
    if target - x in seen:
        return [seen[target-x], i]
    seen[x] = i

# Brute force O(n²) — max subarray
# → O(n) with Kadane's
curr = res = nums[0]
for x in nums[1:]:
    curr = max(x, curr + x)
    res = max(res, curr)

# Key question before any nested loop:
# "Can I precompute something in one pass
#  to avoid the inner loop entirely?"`,
        complexity: [["Nested loop", "O(n²)"], ["With precompute", "O(n)"]],
        mistake: "Before writing a nested loop, ask: can I precompute with a prefix sum, sorted order, or hashmap?",
      },
    ],
  },

  returning: {
    color: "#f472b6",
    intro: "How you return values is as important as how you compute them.",
    subsections: [
      {
        title: "Returning Arrays, Indices, Tuples",
        body: `# Return array
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target-n], i]
    return []   # always return same type!

# Return index (-1 = not found convention)
def find(nums, target):
    for i, n in enumerate(nums):
        if n == target: return i
    return -1

# Return tuple — implicit
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max(nums)   # unpack

# Return multiple values
def partition(arr, l, r):
    # ... logic ...
    return l, r`,
        complexity: [],
        mistake: "Always return the SAME TYPE from all branches. Returning a list sometimes and None other times causes crashes at the call site.",
      },
      {
        title: "Early Return vs Collecting Results",
        body: `# Early return — first match is enough
def contains_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen: return True   # exit immediately
        seen.add(n)
    return False

# Collecting — need ALL results
def find_all_duplicates(nums):
    seen = set()
    result = []
    for n in nums:
        if n in seen:
            result.append(n)   # collect, keep going
        seen.add(n)
    return result

# DFS short-circuit
def dfs(node, target):
    if not node: return False
    if node.val == target: return True
    return dfs(node.left, target) or dfs(node.right, target)`,
        complexity: [],
        mistake: "Using 'collect then return' when 'early return' works wastes time. Using 'early return' when you need ALL results gives wrong answers.",
      },
      {
        title: "Common Return Pitfalls",
        body: `# Pitfall 1: Returning inside loop when you shouldn't
def max_subarray(nums):
    curr = res = nums[0]
    for x in nums[1:]:
        curr = max(x, curr + x)
        res = max(res, curr)
        # DON'T return here — need to see all elements
    return res    # return AFTER loop

# Pitfall 2: Missing return path
def solve(nums):
    if not nums: return 0
    for n in nums:
        if n > 0: return n
    return -1   # MUST have this — all nums <= 0 case

# Pitfall 3: Mutable default argument
def append_to(val, lst=[]):   # lst shared across calls!
    lst.append(val)
    return lst

# Fix:
def append_to(val, lst=None):
    if lst is None: lst = []
    lst.append(val)
    return lst`,
        complexity: [],
        mistake: "Mutable default arguments (def f(lst=[])) are shared across ALL calls to the function. Always use None as default.",
      },
    ],
  },

  prefix: {
    color: "#818cf8",
    intro: "Prefix sums convert range-sum queries from O(n) to O(1). One of the highest-leverage techniques.",
    subsections: [
      {
        title: "Running Sum",
        body: `nums = [1, 2, 3, 4, 5]

# Running total as you iterate
total = 0
for n in nums:
    total += n    # total = 1, 3, 6, 10, 15

# Use case: subarray sum = k
prefix = 0
freq = {0: 1}    # ← critical: init with 0
count = 0
for n in nums:
    prefix += n
    count += freq.get(prefix - k, 0)
    freq[prefix] = freq.get(prefix, 0) + 1
return count`,
        complexity: [["Running sum", "O(n) time, O(1) space"]],
        mistake: "Initialize freq = {0: 1}. Without it, subarrays starting at index 0 are missed entirely.",
      },
      {
        title: "Prefix Sum Array",
        body: `nums = [1, 2, 3, 4, 5]

# Build — O(n)
prefix = [0] * (len(nums) + 1)
for i, n in enumerate(nums):
    prefix[i+1] = prefix[i] + n
# prefix = [0, 1, 3, 6, 10, 15]

# Range sum query — O(1) after O(n) build
def range_sum(l, r):
    return prefix[r+1] - prefix[l]

# Sum of indices 1..3 = 2+3+4 = 9
range_sum(1, 3)   # prefix[4] - prefix[1] = 10 - 1 = 9

# Why size n+1?
# prefix[i] = sum of first i elements = sum(nums[0..i-1])
# Makes the formula clean: prefix[r+1] - prefix[l]`,
        complexity: [["Build", "O(n)"], ["Query", "O(1)"]],
        mistake: "Range sum is prefix[r+1] - prefix[l], NOT prefix[r] - prefix[l]. Off-by-one here is extremely common.",
      },
      {
        title: "Difference Array — Range Updates",
        body: `# Apply +val to nums[l..r] efficiently
n = 5
diff = [0] * (n + 1)

def range_add(l, r, val):
    diff[l] += val
    diff[r+1] -= val    # undo AFTER range

# Apply updates in O(1) each
range_add(0, 2, 3)    # +3 to indices 0,1,2
range_add(1, 4, 1)    # +1 to indices 1,2,3,4

# Reconstruct final array — O(n)
result = []
running = 0
for i in range(n):
    running += diff[i]
    result.append(running)
# result = [3, 4, 4, 1, 1]

# Use cases: LC 1893, 1109, 370
# "apply k range updates, return final array"`,
        complexity: [["Range update", "O(1)"], ["Reconstruct", "O(n)"]],
        mistake: "diff[r+1] -= val, not diff[r]. The undo happens at r+1 (the element AFTER the range ends).",
      },
      {
        title: "When to Use Prefix Sums",
        body: `# Use prefix when:
# 1. Multiple range sum queries on static array
# 2. "Number of subarrays with sum = k"
# 3. Pivot index (left sum == right sum)

# Pivot index — O(n), O(1) space
def pivot_index(nums):
    total = sum(nums)
    left = 0
    for i, n in enumerate(nums):
        # right = total - left - nums[i]
        if left == total - left - n: return i
        left += n
    return -1

# Subarray sum = k — O(n)
def subarray_sum(nums, k):
    count = prefix = 0
    freq = {0: 1}
    for n in nums:
        prefix += n
        count += freq.get(prefix - k, 0)
        freq[prefix] = freq.get(prefix, 0) + 1
    return count`,
        complexity: [["Prefix + map", "O(n) time, O(n) space"]],
        mistake: "For subarray sum = k, you MUST use a hashmap of prefix sums. The array alone isn't enough — you need O(1) lookup of 'have I seen prefix-k before?'",
      },
    ],
  },

  micro: {
    color: "#fb923c",
    intro: "Small techniques that appear in almost every medium-hard problem. Internalize them.",
    subsections: [
      {
        title: "Sentinel Values",
        body: `# Infinity
min_val = float('inf')
max_val = float('-inf')

# Use for comparison initialization
best = float('inf')
for cost in costs:
    best = min(best, cost)

# Dummy node in linked list
dummy = ListNode(0)
dummy.next = head
# ... process ...
return dummy.next   # skips dummy

# Boundary check shorthand for matrices
def neighbors(r, c, rows, cols):
    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc`,
        complexity: [],
        mistake: "float('inf') - float('inf') = nan. float('inf') + float('inf') = inf. Don't subtract infinities.",
      },
      {
        title: "Tuple Comparisons & Tie-Breaking",
        body: `# Python compares tuples lexicographically
(1, 5) < (2, 3)   # True — first element decides
(1, 5) < (1, 8)   # True — tie on first, second decides

# In heap — always add unique int as tiebreaker
import heapq
heapq.heappush(heap, (priority, idx, data))
# idx breaks ties when priority is equal

# Multi-key sort
students.sort(key=lambda x: (x.grade, x.name))

# Return tuple — clean multi-value returns
def bounds(nums):
    return min(nums), max(nums)

lo, hi = bounds(nums)`,
        complexity: [["Tuple compare", "O(k) until first difference"]],
        mistake: "Tuple comparison crashes if elements are uncomparable (custom objects without __lt__). Always add a unique int tiebreaker in heaps.",
      },
      {
        title: "Off-By-One Errors",
        body: `arr = [1,2,3,4,5]   # indices 0..4 = len-1

# range — end is EXCLUSIVE
range(5)            # 0,1,2,3,4 — NOT 5
range(n-1, -1, -1)  # n-1 down to 0 — NOT -1

# Window size
l, r = 2, 4   # indices 2,3,4 → size = r - l + 1 = 3

# Prefix sum — range l to r inclusive
prefix[r+1] - prefix[l]   # NOT prefix[r] - prefix[l]

# Binary search midpoint
mid = l + (r - l) // 2   # avoids overflow

# String slice — end exclusive
s[l:r]      # does NOT include index r
s[l:r+1]    # includes index r`,
        complexity: [],
        mistake: "When unsure, trace on a 3-element array manually. Most off-by-one bugs are found by testing l=0, r=2.",
      },
      {
        title: "Boundary Checks & Safe Access",
        body: `# Safe index access
def safe_get(arr, i):
    return arr[i] if 0 <= i < len(arr) else None

# Matrix bounds check
def in_bounds(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

# All 4 directions
for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
    nr, nc = r+dr, c+dc
    if in_bounds(nr, nc, rows, cols):
        visit(grid, nr, nc)

# Linked list — always check outer before inner
# WRONG: if node.next.val == x
# RIGHT: if node and node.next and node.next.val == x`,
        complexity: [],
        mistake: "Always check node before node.next. 'if node.next' crashes if node is None.",
      },
      {
        title: "Avoiding Unnecessary Copies",
        body: `# SLOW string building O(n²)
s = ""
for c in chars: s += c

# FAST O(n)
s = ''.join(chars)

# arr[:] creates a copy — O(n) space
rev = arr[::-1]         # new list

# reversed() doesn't copy — O(1) space
for x in reversed(arr): # iterate backward, no copy
    ...

# Lists are passed by REFERENCE
def bad(arr):
    arr.append(1)   # modifies caller's list!

def good(arr):
    arr = arr[:]    # local copy — safe
    arr.append(1)`,
        complexity: [],
        mistake: "Lists passed to functions are references. If you modify them, the caller's list changes. Copy when needed: arr = arr[:]",
      },
      {
        title: "Set Membership & Early Exits",
        body: `# O(1) vs O(n) inside loop
seen = []
if x in seen:   # O(n) — BAD inside loop

seen = set()
if x in seen:   # O(1) — GOOD

# Convert before loop, not inside
blocked = set(blocked_list)      # O(n) once
for x in data:
    if x in blocked: skip()      # O(1) each

# any() / all() — short-circuit
any(x > 0 for x in nums)   # stops at first True
all(x > 0 for x in nums)   # stops at first False

# for/else — runs only if no break
for n in nums:
    if invalid(n): break
else:
    return "all valid"   # no break hit`,
        complexity: [["'x' in set", "O(1)"], ["'x' in list", "O(n)"]],
        mistake: "Sets are unordered — no indexing. If you need s[0], use a sorted list instead.",
      },
    ],
  },

  templates: {
    color: "#2dd4bf",
    intro: "These templates cover 90% of LeetCode solutions. Memorize the structure, fill in the logic.",
    subsections: [
      {
        title: "Frequency Counting",
        body: `from collections import Counter, defaultdict

# Counter — best for most cases
freq = Counter(nums)
freq[x]               # 0 if missing, no KeyError
freq.most_common(k)   # top k

# defaultdict — when building incrementally
freq = defaultdict(int)
for x in nums: freq[x] += 1

# Fixed alphabet array — fastest for a-z
freq = [0] * 26
for c in s:
    freq[ord(c) - ord('a')] += 1

# Anagram check
Counter(s) == Counter(t)      # O(n)
sorted(s) == sorted(t)        # O(n log n)`,
        complexity: [["Build", "O(n)"], ["Lookup", "O(1)"]],
        mistake: "For a-z only problems, the 26-element array is faster and uses less memory than a hashmap.",
      },
      {
        title: "Two Pointer Templates",
        body: `# Opposite ends
l, r = 0, len(arr) - 1
while l < r:
    if should_shrink_left(arr[l], arr[r]): l += 1
    else: r -= 1

# Fast/slow
slow = 0
for fast in range(len(arr)):
    if keep(arr[fast]):
        arr[slow] = arr[fast]
        slow += 1
return slow   # new length

# Merge two sorted arrays
i = j = 0
result = []
while i < len(a) and j < len(b):
    if a[i] <= b[j]: result.append(a[i]); i += 1
    else: result.append(b[j]); j += 1
result.extend(a[i:]); result.extend(b[j:])`,
        complexity: [["Two pointer", "O(n) time, O(1) space"]],
        mistake: "while l < r not l <= r. When l == r you're at the same element — no valid pair.",
      },
      {
        title: "Sliding Window Templates",
        body: `# Fixed window
window = sum(nums[:k])
res = window
for i in range(k, len(nums)):
    window += nums[i] - nums[i-k]   # slide
    res = max(res, window)

# Variable window (maximize)
l = res = 0
state = {}
for r in range(len(s)):
    # add s[r] to state
    state[s[r]] = state.get(s[r], 0) + 1
    while invalid(state):
        # remove s[l] from state
        state[s[l]] -= 1
        if state[s[l]] == 0: del state[s[l]]
        l += 1
    res = max(res, r - l + 1)`,
        complexity: [["Sliding window", "O(n)"]],
        mistake: "Record answer AFTER shrinking. Window size = r - l + 1.",
      },
      {
        title: "Prefix Sum Templates",
        body: `# Build prefix array
prefix = [0] * (len(nums) + 1)
for i, n in enumerate(nums):
    prefix[i+1] = prefix[i] + n

# Range sum O(1)
range_sum = prefix[r+1] - prefix[l]

# Subarray sum = k
count = prefix = 0
seen = {0: 1}
for n in nums:
    prefix += n
    count += seen.get(prefix - k, 0)
    seen[prefix] = seen.get(prefix, 0) + 1

# Pivot index
total = sum(nums); left = 0
for i, n in enumerate(nums):
    if left == total - left - n: return i
    left += n`,
        complexity: [["Build", "O(n)"], ["Query", "O(1)"]],
        mistake: "Always initialize seen = {0: 1} for the subarray sum pattern.",
      },
      {
        title: "BFS / DFS Templates",
        body: `from collections import deque

# BFS
def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)     # add when ENQUEUING
                queue.append(nei)

# DFS recursive
def dfs(node, visited, graph):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(nei, visited, graph)

# Matrix BFS (level by level)
queue = deque([(r, c)])
visited = {(r, c)}
dist = 0
while queue:
    for _ in range(len(queue)):    # process level
        r, c = queue.popleft()
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r+dr, c+dc
            if in_bounds(nr, nc) and (nr,nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))
    dist += 1`,
        complexity: [["BFS/DFS", "O(V+E)"]],
        mistake: "Mark visited WHEN ENQUEUING, not when dequeuing. Dequeue-time marking allows duplicates into the queue → slower.",
      },
      {
        title: "Binary Search Templates",
        body: `# Exact search
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: l = mid + 1
        else: r = mid - 1
    return -1

# First True in [F,F,F,T,T,T]
lo, hi = 0, n
while lo < hi:
    mid = (lo + hi) // 2
    if condition(mid): hi = mid
    else: lo = mid + 1
return lo

# Binary search on ANSWER
# "find minimum k such that feasible(k)"
lo, hi = min_possible, max_possible
while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid): hi = mid
    else: lo = mid + 1`,
        complexity: [["Binary search", "O(log n)"]],
        mistake: "Use while l <= r for exact search. Use while l < h for boundary/insertion point search.",
      },
      {
        title: "Monotonic Stack Template",
        body: `# Next greater element (left to right)
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []   # stores indices

    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    return result

# Daily temperatures
def dailyTemperatures(temps):
    result = [0] * len(temps)
    stack = []
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            result[j] = i - j    # days until warmer
        stack.append(i)
    return result

# Decreasing stack → stores next SMALLER element
# Increasing stack → stores next LARGER element`,
        complexity: [["Monotonic stack", "O(n) — each element pushed/popped once"]],
        mistake: "Stack stores INDICES (usually), not values. You need the index to compute distance or fill result arrays.",
      },
    ],
  },
};

function ComplexityBadge({ label, val }) {
  return (
    <span style={{
      display: "inline-flex", gap: 6, alignItems: "center",
      background: "#0d1117", border: "1px solid #1e2a3a",
      borderRadius: 6, padding: "3px 10px", fontSize: "0.72rem",
      fontFamily: "inherit", marginRight: 6, marginBottom: 6,
    }}>
      <span style={{ color: "#666" }}>{label}</span>
      <span style={{ color: "#22d3ee", fontWeight: 700 }}>{val}</span>
    </span>
  );
}

function MistakeBox({ text }) {
  return (
    <div style={{
      background: "#1a0a0a", border: "1px solid #7f1d1d",
      borderLeft: "3px solid #ef4444",
      borderRadius: 6, padding: "10px 14px",
      marginTop: 10,
    }}>
      <span style={{ color: "#ef4444", fontWeight: 700, fontSize: "0.75rem" }}>⚠ COMMON MISTAKE  </span>
      <span style={{ color: "#fca5a5", fontSize: "0.78rem", fontFamily: "'Sora', sans-serif", lineHeight: 1.5 }}>{text}</span>
    </div>
  );
}

function Subsection({ sub, color }) {
  const [open, setOpen] = useState(false);
  return (
    <div style={{ marginBottom: 8, border: "1px solid #1a2030", borderRadius: 10, overflow: "hidden" }}>
      <button
        onClick={() => setOpen(o => !o)}
        style={{
          width: "100%", textAlign: "left", background: open ? "#0d1420" : "#090d14",
          border: "none", padding: "12px 18px", cursor: "pointer",
          display: "flex", justifyContent: "space-between", alignItems: "center",
          transition: "background 0.15s",
        }}
      >
        <span style={{ color: open ? color : "#aaa", fontSize: "0.85rem", fontWeight: 600, fontFamily: "'Sora', sans-serif" }}>
          {sub.title}
        </span>
        <span style={{ color: color, fontSize: "1rem", opacity: open ? 1 : 0.4 }}>{open ? "−" : "+"}</span>
      </button>

      {open && (
        <div style={{ padding: "4px 18px 18px", background: "#090d14" }}>
          <pre style={{
            background: "#05080e", border: "1px solid #151e2e", borderRadius: 8,
            padding: "14px 16px", fontSize: "0.76rem", lineHeight: 1.75,
            color: "#c9d1d9", overflowX: "auto", fontFamily: "'JetBrains Mono', monospace",
            margin: "10px 0",
          }}>{sub.body}</pre>

          {sub.complexity.length > 0 && (
            <div style={{ marginBottom: 8 }}>
              {sub.complexity.map(([l, v]) => (
                <ComplexityBadge key={l} label={l} val={v} />
              ))}
            </div>
          )}

          {sub.mistake && <MistakeBox text={sub.mistake} />}
        </div>
      )}
    </div>
  );
}

export default function Guide() {
  const [active, setActive] = useState("arrays");
  const sec = content[active];

  return (
    <div style={{ minHeight: "100vh", background: "#060a0f", fontFamily: "'JetBrains Mono', monospace", display: "flex", flexDirection: "column" }}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;600;700&family=Sora:wght@400;600;700&display=swap');
        * { box-sizing: border-box; margin: 0; padding: 0; }
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: #060a0f; }
        ::-webkit-scrollbar-thumb { background: #1e2a3a; border-radius: 3px; }
        .nav-pill { transition: all 0.15s; }
        .nav-pill:hover { opacity: 1 !important; }
      `}</style>

      {/* Header */}
      <div style={{ background: "#070c12", borderBottom: "1px solid #111e2e", padding: "20px 24px 0" }}>
        <div style={{ maxWidth: 860, margin: "0 auto" }}>
          <h1 style={{ fontSize: "1.5rem", fontFamily: "'Sora', sans-serif", fontWeight: 700, color: "#fff", marginBottom: 4 }}>
            <span style={{ color: sec.color }}>⬡</span> LeetCode Primitives
          </h1>
          <p style={{ fontSize: "0.75rem", color: "#3a4a5a", marginBottom: 16 }}>
            Implementation-level reference — arrays · strings · hashmaps · loops · patterns
          </p>

          {/* Nav */}
          <div style={{ display: "flex", gap: 4, flexWrap: "wrap", paddingBottom: 0 }}>
            {sections.map(s => (
              <button
                key={s.id}
                className="nav-pill"
                onClick={() => setActive(s.id)}
                style={{
                  padding: "8px 14px", border: "none", borderRadius: "8px 8px 0 0",
                  background: active === s.id ? "#0d1520" : "transparent",
                  color: active === s.id ? s.color : "#445",
                  cursor: "pointer", fontSize: "0.72rem", fontFamily: "'Sora', sans-serif",
                  fontWeight: 600, opacity: active === s.id ? 1 : 0.7,
                  borderTop: active === s.id ? `2px solid ${s.color}` : "2px solid transparent",
                }}
              >
                {s.icon} {s.label}
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Content */}
      <div style={{ flex: 1, maxWidth: 860, margin: "0 auto", width: "100%", padding: "24px 24px" }}>
        <div style={{
          background: "#07090e", border: `1px solid ${sec.color}22`,
          borderLeft: `3px solid ${sec.color}`,
          borderRadius: 10, padding: "12px 18px", marginBottom: 20,
        }}>
          <p style={{ color: "#8899aa", fontSize: "0.82rem", fontFamily: "'Sora', sans-serif", lineHeight: 1.5 }}>
            {sec.intro}
          </p>
        </div>

        {sec.subsections.map(sub => (
          <Subsection key={sub.title} sub={sub} color={sec.color} />
        ))}
      </div>
    </div>
  );
}
