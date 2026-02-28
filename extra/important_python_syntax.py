from collections import deque, defaultdict, Counter
import heapq
from bisect import bisect_left, bisect_right

"""
IMPORTANT PYTHON SYNTAX FOR LEETCODE - ARRAYS & HASHMAPS
Build muscle memory for these patterns
"""

# ============================================================================
# 1. ARRAYS - COMMON OPERATIONS
# ============================================================================

arr = [1, 2, 3, 4, 5]

# Initialization
zeros = [0] * n                    # Create array of n zeros
grid = [[0] * cols for _ in range(rows)]  # 2D array (CORRECT way)
# WRONG: [[0] * cols] * rows      # This creates shallow copies!

# Iteration patterns
for i in range(len(arr)):          # Index only
    pass

for val in arr:                    # Value only
    pass

for i, val in enumerate(arr):      # Both index and value
    pass

for i in range(len(arr) - 1, -1, -1):  # Reverse iteration
    pass



# Slicing (creates new list)
arr[:]        # Copy entire array
arr[1:4]      # Elements from index 1 to 3 (4 excluded)
arr[:3]       # First 3 elements
arr[3:]       # From index 3 to end
arr[-3:]      # Last 3 elements
arr[::-1]     # Reverse array
arr[::2]      # Every 2nd element



# Common array methods
arr.append(x)         # Add to end - O(1)
arr.pop()             # Remove from end - O(1)
arr.pop(i)            # Remove at index i - O(n)
arr.insert(i, x)      # Insert x at index i - O(n)
arr.remove(x)         # Remove first occurrence of x - O(n)
arr.reverse()         # Reverse in place - O(n)
arr.sort()            # Sort in place - O(n log n)
sorted(arr)           # Return new sorted list - O(n log n)
sorted(arr, reverse=True)  # Sort descending


# List comprehensions (Pythonic and fast)
squares = [x**2 for x in arr]
evens = [x for x in arr if x % 2 == 0]
pairs = [(i, val) for i, val in enumerate(arr)]



# ============================================================================
# 2. HASHMAP (dict) - FOUNDATION
# ============================================================================

# Initialization
d = {}
d = dict()


# Common operations
d[key] = value                    # Set
val = d[key]                      # Get (raises KeyError if missing)
val = d.get(key)                  # Returns None if missing
val = d.get(key, default_val)     # Returns default_val if missing
if key in d:                      # Check existence - O(1)
    pass
d.pop(key)                        # Remove and return value
d.pop(key, default)               # Remove or return default if missing
del d[key]                        # Remove key


# Iteration
for key in d:                     # Iterate over keys
    pass

for key, val in d.items():        # Iterate over key-value pairs
    pass

for val in d.values():            # Iterate over values
    pass

# Useful patterns
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1    # Manual counting

# Dictionary comprehension
char_to_idx = {char: i for i, char in enumerate(s)}

freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
    
char_to_idx = {char: i for i, char in enumerate(s)}
 
 
freq = {}

for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Alternatively:

for char in s:
    freq[char] = freq.get(char, 0) + 1

# Comparison with alternatives:                                                                                                                               
                                                                                                                                                              
  # Method 1: Regular dict with .get() (what you have)                                                                                                        
freq = {}                                                                                                                                                     for char in s:                                                                                                                                              
    
    freq[char] = freq.get(char, 0) + 1                                                                                                                      
                                                                                                                                                              
  # Method 2: defaultdict (even cleaner, no .get() needed)                                                                                                    
from collections import defaultdict                                                                                                                         
  
freq = defaultdict(int)                                                                                                                                     
for char in s:                                                                                                                                              
  freq[char] += 1  # No need for .get(), automatically starts at 0                                                                                        
                                                                                                                                                              
  # Method 3: Counter (simplest)                                                                                                                              
from collections import Counter                                                                                                                             
freq = Counter(s)  # Done in one line!                                                                                                                      
                                                                                                                                                              
# All three produce the same result, but Method 1 with .get() is great to know because it works with regular dicts and doesn't require imports. 

# ============================================================================
# 3. defaultdict - AUTO-INITIALIZE MISSING KEYS
# ============================================================================

"""
defaultdict automatically provides a default value for missing keys.
This prevents KeyError and eliminates the need for 'if key in dict' checks.

Common use cases:
- Counting: defaultdict(int) starts at 0
- Grouping: defaultdict(list) starts with empty list
- Graph adjacency: defaultdict(list) for edges
- Unique collections: defaultdict(set)
"""

from collections import defaultdict

# PATTERN 1: Counting (alternative to Counter for dynamic updates)
freq = defaultdict(int)           # Default value: 0
for char in "hello":
    freq[char] += 1               # No need to check if key exists!
# Result: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# PATTERN 2: Grouping items into lists
groups = defaultdict(list)        # Default value: []
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
for word in words:
    key = ''.join(sorted(word))   # Group anagrams
    groups[key].append(word)      # No need to initialize list!
# Result: {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}

# PATTERN 3: Graph adjacency list
graph = defaultdict(list)
edges = [[1,2], [1,3], [2,4]]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)            # Undirected graph

# PATTERN 4: Unique collections per key
seen = defaultdict(set)           # Default value: set()
for i, num in enumerate(arr):
    seen[num].add(i)              # Store all indices where num appears

# PATTERN 5: Nested defaultdict
nested = defaultdict(lambda: defaultdict(int))
nested[row][col] += 1             # 2D sparse matrix

# Converting to regular dict (for clean output)
regular_dict = dict(freq)


# ============================================================================
# 4. Counter - SPECIALIZED FOR COUNTING
# ============================================================================

"""
Counter is a dict subclass designed specifically for counting hashable objects.
It provides convenient methods for frequency analysis.

TC = O(n), iterates through every element once to count frequencies
SC = O(k), k=number of unique elements, stores one key-value pair per unique element

Counter is optimized C code under the hood, so while the Big O is the same, it's often slightly faster in practice than a Python loop with 
dict/defaultdict.
"""

from collections import Counter

# INITIALIZATION
arr = [1, 2, 2, 3, 3, 3]
s = "aabbcc"

count = Counter(arr)              # From list: Counter({3: 3, 2: 2, 1: 1})
count = Counter(s)                # From string: Counter({'a': 2, 'b': 2, 'c': 2})
count = Counter()                 # Empty counter
count = Counter({'a': 3, 'b': 2}) # From dict

# ACCESSING COUNTS
count['a']                        # Get count (returns 0 if missing, not KeyError!)
count.get('a', 0)                 # Also works

# MOST COMMON OPERATIONS
count.most_common()               # List of (element, count) sorted by count desc
count.most_common(3)              # Top 3 most common
count.most_common()[-1]           # Least common element

# Example: Top K Frequent Elements
nums = [1,1,1,2,2,3]
k = 2
counter = Counter(nums)
top_k = [num for num, freq in counter.most_common(k)]  # [1, 2]

# ARITHMETIC OPERATIONS
c1 = Counter(['a', 'b', 'b'])     # Counter({'b': 2, 'a': 1})
c2 = Counter(['b', 'c', 'c'])     # Counter({'c': 2, 'b': 1})

c1 + c2                           # Add: Counter({'b': 3, 'c': 2, 'a': 1})
c1 - c2                           # Subtract (keep only positive): Counter({'a': 1, 'b': 1})
c1 & c2                           # Intersection (min): Counter({'b': 1})
c1 | c2                           # Union (max): Counter({'b': 2, 'c': 2, 'a': 1})

# UPDATE OPERATIONS
count = Counter("hello")
count.update("world")             # Add more counts
count.subtract("lo")              # Subtract counts (can go negative)

# CHECKING IF TWO STRINGS ARE ANAGRAMS
def is_anagram(s, t):
    return Counter(s) == Counter(t)

# CHECKING IF STRING CAN FORM PALINDROME
def can_form_palindrome(s):
    counts = Counter(s)
    odd_count = sum(1 for c in counts.values() if c % 2 == 1)
    return odd_count <= 1

# FINDING UNIQUE ELEMENTS
count = Counter(arr)
unique = [x for x in count if count[x] == 1]

# Converting to list of elements (with repetition)
count = Counter({'a': 3, 'b': 2})
elements = list(count.elements())  # ['a', 'a', 'a', 'b', 'b']

# Getting keys/values/items (inherits from dict)
count.keys()
count.values()
count.items()


# ============================================================================
# 5. WHEN TO USE WHAT?
# ============================================================================

"""
REGULAR DICT:
- When you need to check if key exists before operating
- When default value logic is complex
- General key-value mapping

defaultdict(int):
- Counting with dynamic updates
- When you need to increment/decrement frequently
- Building frequency maps on the fly

defaultdict(list):
- Grouping items (anagrams, similar values)
- Graph adjacency lists
- Collecting multiple values per key

defaultdict(set):
- Storing unique items per key
- Graph problems with unique edges
- Deduplication per category

Counter:
- Pure frequency counting
- Finding most/least common elements
- Set operations on multisets (union, intersection)
- Comparing frequencies (anagrams, subsets)
- When you need arithmetic operations on counts
"""


# ============================================================================
# 6. COMMON LEETCODE PATTERNS
# ============================================================================

# PATTERN: Two Sum (dict for O(1) lookup)
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# PATTERN: Group Anagrams (defaultdict for grouping)
def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return list(groups.values())

# PATTERN: Valid Anagram (Counter comparison)
def is_anagram(s, t):
    return Counter(s) == Counter(t)

# PATTERN: Top K Frequent (Counter.most_common)
def top_k_frequent(nums, k):
    counter = Counter(nums)
    return [num for num, freq in counter.most_common(k)]

# PATTERN: First Unique Character (Counter for frequency)
def first_uniq_char(s):
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1

# PATTERN: Subarray Sum Equals K (defaultdict for prefix sums)
def subarray_sum(nums, k):
    prefix_count = defaultdict(int)
    prefix_count[0] = 1
    curr_sum = 0
    result = 0
    for num in nums:
        curr_sum += num
        if curr_sum - k in prefix_count:
            result += prefix_count[curr_sum - k]
        prefix_count[curr_sum] += 1
    return result


# ============================================================================
# 7. TIME COMPLEXITY CHEAT SHEET
# ============================================================================

"""
DICT / defaultdict / Counter (all use hash tables):
- Access/Insert/Delete: O(1) average, O(n) worst case
- 'in' operator: O(1) average
- Iteration: O(n)

Counter specific:
- most_common(): O(n log n) due to sorting
- Arithmetic operations: O(n)

ARRAY:
- Access by index: O(1)
- Append/Pop (end): O(1) amortized
- Insert/Delete (middle): O(n)
- Search (unsorted): O(n)
- Search (sorted): O(log n) with binary search
- Sort: O(n log n)
- Reverse: O(n)
"""
