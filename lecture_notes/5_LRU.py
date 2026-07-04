"""
LRU cache
least recently used cache
explanation:
use a doubly linked list to store the data, 
and a hash map to store the key and the node in the linked list.
"""


class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None



class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.data = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.data.get(key)
        if node is None:
            return -1
        self.remove(node)
        self.add_to_head(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.data.get(key)
        if node is not None:
            self.remove(node)
            self.add_to_head(node)
            node.value = value
            return
        else:
            if len(self.data) >= self.capacity:
                node = self.tail.prev
                self.remove(node)
                del self.data[node.key]
        node = Node(key, value)
        self.add_to_head(node)
        self.data[key] = node
        return



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
