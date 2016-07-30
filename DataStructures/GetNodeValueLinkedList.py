#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
    cursor = head
    values = []
    while cursor.next:
        values.append(cursor.data)
        cursor = cursor.next
    values.append(cursor.data)
    index = position + 1
    return values[-index]
  