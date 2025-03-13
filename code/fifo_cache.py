import heapq
from typing import Any, Dict, List, Tuple, Optional


class FIFOCache:
    """
    A simple FIFO cache implementation using a min heap.
    Elements are prioritized solely by insertion order (counter).
    """

    def __init__(self, capacity: int = 100):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")

        self.capacity = capacity
        self.heap: List[Tuple[int, Any]] = []  # (counter, key) for eviction
        self.cache: Dict[Any, Any] = {}  # actual cache
        self.counter = 0

    def __len__(self) -> int:
        return len(self.cache)

    def put(self, key: Any, value: Any) -> None:
        """
        Add or update an item in the cache.
        If the cache is full, the oldest item is evicted.

        Args:
            key: The key to store the value under
            value: The value to store
        """
        # If key already exists, remove it first
        if key in self.cache:
            self._remove(key)

        # If cache is full, evict the oldest item
        if len(self.cache) >= self.capacity:
            self._evict()

        # Create the entry
        entry = (self.counter, key)
        self.counter += 1

        # Add to the data structures
        self.cache[key] = value
        heapq.heappush(self.heap, entry)

    def get(self, key: Any) -> Optional[Any]:
        """
        Retrieve an item from the cache by key.
        Returns None if the key doesn't exist.

        Args:
            key: The key to look up

        Returns:
            The associated value or None if not found
        """
        return self.cache.get(key)

    def _remove(self, key: Any) -> None:
        """
        Remove an item from the cache by key.

        Args:
            key: The key to remove
        """
        # Remove from data dictionary
        if key in self.cache:
            del self.cache[key]

            # Find and remove from heap
            # Note: This is inefficient but simpler than marking
            self.heap = [(c, k) for c, k in self.heap if k != key]
            heapq.heapify(self.heap)

    def _evict(self) -> None:
        """
        Evict the oldest item from the cache.
        """
        while self.heap:
            _, key = heapq.heappop(self.heap)
            if key in self.cache:
                del self.cache[key]
                break

    def peek_oldest(self) -> Tuple[Any, Any]:
        """
        Return the (key, value) pair of the oldest item without removing it.

        Returns:
            A tuple of (key, value) for the oldest item

        Raises:
            KeyError: If the cache is empty
        """
        if not self.heap:
            raise KeyError("Cannot peek from an empty cache")

        # Get the oldest entry (lowest counter)
        _, key = self.heap[0]
        return key, self.cache[key]

    def pop_oldest(self) -> Tuple[Any, Any]:
        """
        Remove and return the (key, value) pair of the oldest item.

        Returns:
            A tuple of (key, value) for the oldest item

        Raises:
            KeyError: If the cache is empty
        """
        if not self.heap:
            raise KeyError("Cannot pop from an empty cache")

        _, key = heapq.heappop(self.heap)
        value = self.cache.pop(key)
        return key, value

    def clear(self) -> None:
        """Clear all items from the cache."""
        self.heap = []
        self.cache = {}


# Example usage
if __name__ == "__main__":
    cache = FIFOCache(capacity=3)

    # Add some items
    cache.put("A", "Value A")
    cache.put("B", "Value B")
    cache.put("C", "Value C")

    # Cache is now full, adding another item will evict the oldest (A)
    cache.put("D", "Value D")

    print(f"Value for key 'A': {cache.get('A')}")  # None (evicted)
    print(f"Value for key 'B': {cache.get('B')}")  # Value B

    # Peek at the oldest item
    oldest_key, oldest_value = cache.peek_oldest()
    print(f"Oldest item: {oldest_key} -> {oldest_value}")  # B -> Value B

    # Pop items in FIFO order
    while len(cache) > 0:
        key, value = cache.pop_oldest()
        print(f"Popped: {key} -> {value}")

    # Expected output:
    # Popped: B -> Value B
    # Popped: C -> Value C
    # Popped: D -> Value D
