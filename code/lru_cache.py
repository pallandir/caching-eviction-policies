class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class DLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        prev_neighbour = node.prev
        next_neighbour = node.next
        prev_neighbour.next = next_neighbour
        next_neighbour.prev = prev_neighbour

    def remove_tail(self):
        prev_node = self.tail.prev
        self.remove_node(prev_node)
        return prev_node

    def move_front(self, node):
        self.remove_node(node)
        self.add_front(node)

    def display_cache(self):
        node = self.head
        ordered_cache = []
        while node is not None:
            if node.value is not None:
                ordered_cache.append(node.value)
            node = node.next
        print(f"Latest added value : {ordered_cache[0]}", ordered_cache)


class LRUCache:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Cache size must be positive")
        self.size = size
        self.cache = {}
        self.ddl = DLinkedList()

    def __len__(self):
        return len(self.cache)

    def get(self, key):
        if key not in self.cache:
            return None
        node = self.cache.get(key)
        self.ddl.move_front(node)
        return node.value

    def remove_from_cache(self, key):
        if key not in self.cache:
            return False

        node = self.cache.get(key)
        self.ddl.remove_node(node)
        del self.cache[key]
        return True

    def put(self, key, value):
        if key in self.cache:
            node = self.cache.get(key)
            node.value = value
            self.ddl.move_front(node)
            return

        if len(self.cache) >= self.size:
            tail_node = self.ddl.remove_tail()
            del self.cache[tail_node.key]

        new_node = Node(key, value)
        self.ddl.add_front(new_node)
        self.cache[key] = new_node

    def display_cache(self):
        node = self.ddl.head
        ordered_cache = []
        while node is not None:
            if node.value is not None:
                ordered_cache.append(node.value)
            node = node.next
        print(f"Latest added value : {ordered_cache[0]}", ordered_cache)


if __name__ == "__main__":
    cache = LRUCache(size=3)

    # Add some items
    cache.put("A", "Value A")
    cache.put("B", "Value B")
    cache.put("C", "Value C")
    cache.display_cache()

    cache.put("D", "Value D")
    cache.display_cache()

    cache.put("C", "Value C")
    cache.display_cache()

    cache.put("E", "Value E")
    cache.display_cache()
