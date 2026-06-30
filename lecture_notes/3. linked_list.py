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
    
"""
234. Palindrome Linked List
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        def middle(head):
            slow = head
            fast = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        def reverse(head):
            prev = None
            current = head
            while current:
                tmp = current.next
                current.next = prev
                prev = current
                current = tmp
            return prev

        mid = middle(head)
        second = reverse(mid)
        first = head

        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
            
        return True        
    

"""
83. Remove Duplicates from Sorted List
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
        
"""
19. Remove Nth Node From End of List
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        dummy.next = head
        
        first = dummy
        second = dummy

        for i in range(n+1):
            first = first.next

        while first:
            first = first.next
            second = second.next
        second.next = second.next.next

        return dummy.next
    
"""
24. Swap Nodes in Pairs
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        dummy.next = head

        current = dummy
        while current.next and current.next.next:
            first = current.next
            second = current.next.next

            first.next = second.next
            second.next = first
            current.next = second

            current = first

        return dummy.next
    
"""
21. Merge Two Sorted Lists
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy
        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val < p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
        
        if p1:
            current.next = p1
        else:
            current.next = p2

        return dummy.next
    

"""
141. Linked List Cycle
"""
# use two pointers, slow and fast. 
# Move slow by one step and fast by two steps. 
# If there is a cycle, they will eventually meet. 
# If fast reaches the end of the list, there is no cycle.
# Definition for singly-linked list. 
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False