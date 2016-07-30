"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def ReversePrint(head):
    if not head:
        return
    linked_list = []
    cursor = head
    while cursor.next:
        linked_list.append(cursor.data)
        cursor = cursor.next
    linked_list.append(cursor.data)
    while linked_list:
        print(linked_list.pop())