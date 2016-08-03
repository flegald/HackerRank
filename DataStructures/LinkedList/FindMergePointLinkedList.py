"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    s = set()
    cursor = headA
    while cursor.next:
        s.add(cursor.data)
        cursor = cursor.next
    s.add(cursor.data)
    cursor = headB
    while True:
        if cursor.data in s:
            return cursor.data
        cursor = cursor.next
  