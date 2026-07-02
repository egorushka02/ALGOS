class Node:
    def __init__(self, key=0, value=0, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, key):
        """
        :type index: int
        :rtype: int
        """
        current = self.head
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return -1
        
    
    def put(self, key, value):
        current = self.head
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        newNode = Node(
            key=key,
            value=value,
            next=self.head
        )
        self.head = newNode

    def remove(self, key):
        if self.head is None:
            return
        if self.head.key == key:
            self.head = self.head.next
            return
        current = self.head 
        while current.next is not None:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next


class MyHashMap(object):

    def __init__(self):
        self.n = 991
        self.bucket = [MyLinkedList() for _ in range(self.n)]

    def hash(self, x):
        return x % self.n

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        n = self.hash(key)
        self.bucket[n].put(key, value)
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        n = self.hash(key)
        return self.bucket[n].get(key)


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        n = self.hash(key)
        self.bucket[n].remove(key)
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)