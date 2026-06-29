"""
Linked list

head                  tail
[2, *] [5, *] [3, *] [8, ]

operations

search
find n2 with known n0
current = this.head
current = current.next
for i=0; i< index

set new head in begin
new_node = 7
new_node.next = this.head
this.head = new_node
O(1)

set new head between 2 and 1 (exsist heads)
was
[2] -> [5] -> [3] -> [8]
now
[2] -> [5] -> [7] -> [3] -> [8]
old.next = current.next
current.next = new_node(7)
new_node.next = old_next

delete n2
stop at n1
current.next = current.next.next

"""


"""
707. Design linked list
"""

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class MyLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for i in range(index):
            current = current.next
        return current.value
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return
        self.size += 1

        if index == 0:
            new_node = Node(
                value = val,
                next = self.head
            )
            self.head = new_node
            return 
        
        current = self.head
        for i in range(index-1):
            current = current.next
        old_next = current.next
        current.next = Node(
            value = val,
            next = old_next 
        )

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        
        self.size -= 1
        
        if index == 0:
            self.head = self.head.next
            return 
        
        current = self.head
        for i in range(index-1):
            current = current.next
        current.next = current.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


"""
876. Middle of the linked list

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
"""
2095. Delete the Middle Node of a Linked List
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head.next:
            return None
        slow = head
        fast = head.next.next

        while fast and fast.next:
            fast = fast.next.next
            # встал за одну ноду до середины
            slow = slow.next
        slow.next = slow.next.next
        return head
    

"""
206. Reverse Linked List
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        current = head
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev