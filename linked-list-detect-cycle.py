"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    visited = dict()
    if head is None:
        return False
    while(head is not None):
        val = head.data
        if visited.get(val):
            return True
        visited[val] = True
        head = head.next
    return False
    
