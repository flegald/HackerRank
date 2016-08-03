"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def SortedInsert(head, data):
    if not head:
        return Node(data)
    cursor = head
    new_node = Node(data)
    while cursor:
        if new_node.data < cursor.data:
            new_node.next = cursor
            new_node.prev = cursor.prev
            cursor.prev = new_node
            if not new_node.prev:
                return new_node
            new_node.prev.next = new_node
            return head
        if not cursor.next:
            cursor.next = new_node
            new_node.prev = cursor
            return head
        cursor = cursor.next
            
                