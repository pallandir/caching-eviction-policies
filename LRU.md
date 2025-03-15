## LRU cache

An LRU (Least Recently Used) cache follows a simple rule: when the cache reaches its maximum capacity, the least recently used item is removed to make space for new entries.

Unlike a FIFO (First-In, First-Out) cache, where items are removed based on insertion order, an LRU cache updates the position of an item whenever it is accessed. This means that frequently accessed items stay in the cache longer, making LRU more efficient for workloads where recently used data is more likely to be needed again.

Here is an implementation of a LRU cache in python: [LRU cache](code/lru_cache.py)

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

### Implementation

```python
class LRUCache:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Cache size must be positive")
        self.size = size
        self.cache = {}
        self.head = Node()
        self.tail = Node()

        # dummy lru ll setup
        self.head.next = self.tail
        self.tail.prev = self.head

    def __len__(self):
        return len(self.cache)

    ...

    def get(self, key):
        if key not in self.cache:
            return None
        node = self.cache.get(key)
        self._move_front(node)
        return node.value

    def remove_from_cache(self, key):
        if key not in self.cache:
            return False

        node = self.cache.get(key)
        self._remove_node(node)
        del self.cache[key]
        return True

    def put(self, key, value):
        if key in self.cache:
            node = self.cache.get(key)
            node.value = value
            self._move_front(node)
            return

        if len(self.cache) >= self.size:
            tail_node = self._remove_tail()
            del self.cache[tail_node.key]

        new_node = Node(key, value)
        self._add_front(new_node)
        self.cache[key] = new_node
```
