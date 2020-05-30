#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(node): 
      
    # If empty list, return 
    if not node: 
        return None
  
    # Otherwise, swap the next and prev 
    temp = node.next
    node.next = node.prev 
    node.prev = temp 
  
    # If the prev is now None, the list 
    # has been fully reversed 
    if not node.prev: 
        return node 
  
    # Otherwise, keep going 
    return reverse(node.prev) 
def printList(head): 
    while (head != None) : 
        print(head.data, end = " ") 
        head = head.next    
if __name__ == '__main__':
    

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        printList(llist1)
        
