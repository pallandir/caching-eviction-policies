## LRU cache

An LRU (Least Recently Used) cache follows a simple rule: when the cache reaches its maximum capacity, the least recently used item is removed to make space for new entries.

Unlike a FIFO (First-In, First-Out) cache, where items are removed based on insertion order, an LRU cache updates the position of an item whenever it is accessed. This means that frequently accessed items stay in the cache longer, making LRU more efficient for workloads where recently used data is more likely to be needed again.

Here is an implementation of a LRU cache in python:

### How does it works

let's consider this sequence of requests:

```sh
1,2,3,2,4,4,4,4,4,1,4,4,4,4,4,5
```

Assuming a LRU cache with a capacity of 3, the state of the cache evolves as follows:

1.  Initial State: The cache is empty → [].
2.  Request 1: Add 1 → [1].
3.  Request 2: Add 2 → [1, 2].
4.  Request 3: Add 3 → [1, 2, 3].
5.  Request 2: 2 is already in the cache → Move 2 to most recently used → [1, 3, 2].
6.  Request 4: Cache is full → Evict least recently used (1), add 4 → [3, 2, 4].
7.  Request 4 (again): 4 is already in the cache → No change → [3, 2, 4].
8.  Request 1: Cache is full → Evict least recently used (3), add 1 → [2, 4, 1].
9.  Request 5: Cache is full → Evict least recently used (2), add 5 → [4, 1, 5].
