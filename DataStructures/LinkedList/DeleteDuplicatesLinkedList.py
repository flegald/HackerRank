"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
    if not head:
        return
    cursor = head
    while cursor.next:
        if cursor.data == cursor.next.data:
            try:
                cursor.next = cursor.next.next
            except:
                cursor.next = None
        else:
            cursor = cursor.next
    return head
  