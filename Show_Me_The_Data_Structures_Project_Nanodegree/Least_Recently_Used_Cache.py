#Least Recently Used Cache

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = prev

class LRU_cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = tail
        self.tail.prev = head

    def get(self, key):
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.dict:
            self.remove(self.dict[key])
        node = Node(key, value)
        self.add(node)
        self.dict[key] = node
        if len(self.dict) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.dict[node.key]
        return

    def remove(self, node):
        next = node.next
        prev = node.prev
        prev.next = next
        next.prev = prev

    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail
