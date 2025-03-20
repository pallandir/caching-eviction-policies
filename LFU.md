## LFU cache

An LFU (Least Frequently Used) cache is a caching mechanism that removes the least frequently accessed item when the cache reaches its maximum capacity. This ensures that frequently accessed items remain available for longer, optimizing performance in scenarios where repeated access patterns exist.

Here is an implementation of a LFU cache in python: [LFU cache](code/LFU_cache.py)

### Comparison

| **Cache Type**                  | **Eviction Rule**                          | **Behavior**                            |
| ------------------------------- | ------------------------------------------ | --------------------------------------- |
| **FIFO (First-In, First-Out)**  | Removes the oldest item in insertion order | Does not consider access frequency      |
| **LRU (Least Recently Used)**   | Removes the least recently accessed item   | Prioritizes recency but not frequency   |
| **LFU (Least Frequently Used)** | Removes the least accessed item            | Items used frequently stay in the cache |

