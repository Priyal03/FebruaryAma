class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.cap = capacity
        self.left = LinkedNode(0,0)
        self.right=LinkedNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])

        self.hashmap[key]=LinkedNode(key,value)
        self.insert(self.hashmap[key])

        if len(self.hashmap)>self.cap:
            lru_node =self.left.next 
            self.remove(lru_node)
            del self.hashmap[lru_node.key]

    def insert(self,node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev=node
        node.prev = prev
        node.next = nxt

    def remove(self,node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class LinkedNode():
    def __init__(self, key,value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None