class Node:
    def __init__(self, key=0, val=0):
        self.key = key # Storing key helps during eviction
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = {}
        
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.dic:
            self._remove(self.dic[key])
            self._insert(self.dic[key])
            return self.dic[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self._remove(self.dic[key])
        
        self.dic[key] = Node(key, value)
        self._insert(self.dic[key])

        if len(self.dic) > self.cap:
            lru = self.left.next
            self._remove(lru)
            del self.dic[lru.key]