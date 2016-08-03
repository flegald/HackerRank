"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def Reverse(head):
    if not head:
        return
    cursor = head
    while cursor:
        old_previous = cursor.prev
        old_next = cursor.next
        cursor.next = old_previous
        cursor.prev = old_next
        if not old_next:
            head = cursor
            return head
        cursor = old_next
        
        