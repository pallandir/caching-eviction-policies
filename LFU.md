## LFU cache

An LFU (Least Frequently Used) cache is a caching mechanism that removes the least frequently accessed item when the cache reaches its maximum capacity. This ensures that frequently accessed items remain available for longer, optimizing performance in scenarios where repeated access patterns exist.

Here is an implementation of a LFU cache in python: [LFU cache](code/LFU_cache.py)

### Comparison

| **Cache Type**                  | **Eviction Rule**                          | **Behavior**                            |
| ------------------------------- | ------------------------------------------ | --------------------------------------- |
| **FIFO (First-In, First-Out)**  | Removes the oldest item in insertion order | Does not consider access frequency      |
| **LRU (Least Recently Used)**   | Removes the least recently accessed item   | Prioritizes recency but not frequency   |
| **LFU (Least Frequently Used)** | Removes the least accessed item            | Items used frequently stay in the cache |

### How does it works

let's consider this sequence of requests:

```sh
1,2,3,2,4,4,4,4,4,1,4,4,4,4,4,5
```

Assuming a LFU cache with a capacity of 3, the state of the cache evolves as follows:

1.  Initial State → [] (empty cache)
2.  Request 1 → Add 1 → [1]
3.  Request 2 → Add 2 → [1, 2]
4.  Request 3 → Add 3 → [1, 2, 3]
5.  Request 2 → 2 is accessed again → [1, 3, 2] (frequency of 2 increases)
6.  Request 4 → Cache is full; evict 1 (least used), add 4 → [3, 2, 4]
7.  Request 4 → 4 is accessed again (frequency increases) → [3, 2, 4]
8.  Request 1 → Cache is full; evict 3 (least used), add 1 → [2, 4, 1]
9.  Request 5 → Cache is full; evict 2 (least used), add 5 → [4, 1, 5]
