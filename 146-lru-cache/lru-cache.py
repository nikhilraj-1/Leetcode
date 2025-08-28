class LRUCache:
    def __init__(self, capacity: int):
        # Maximum number of items cache can hold
        self.cap = capacity
        # OrderedDict remembers insertion order (and we can move keys on access)
        self.od = OrderedDict()

    def get(self, key: int) -> int:
        # If key not found → return -1
        if key not in self.od:
            return -1
        # Move the key to the end → marks it as recently used
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key: int, value: int) -> None:
        # If key already exists, move it to the end (update recency)
        if key in self.od:
            self.od.move_to_end(key)
        # Insert/Update key with value
        self.od[key] = value
        # If cache exceeds capacity → remove least recently used item (first one)
        if len(self.od) > self.cap:
            self.od.popitem(last=False)   # last=False → pop from the front (LRU)
