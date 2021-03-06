"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    cursor = head
    prev_node = None
    while cursor:
        next_node = cursor.next
        cursor.next = prev_node
        prev_node = cursor
        cursor = next_node
    head = prev_node
    return head
        