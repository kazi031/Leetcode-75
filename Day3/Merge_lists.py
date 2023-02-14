# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
print("Please enter the number of elements in List1: ")
in_a = int(input())
print("Please enter the number of elements in List2: ")
in_b = int(input())

print("Please enter the elements in List1: ")
elem = int(input())
list1 = ListNode(elem, next=None)
temp = list1
for i in range(in_a-1):
    elem = int(input())
    newnode = ListNode(elem,next=None)
    temp.next = newnode
    temp = temp.next

print("Please enter the elements in List2: ")
elem = int(input())
list2 = ListNode(elem, next=None)
temp = list2
for i in range(in_b-1):
    elem = int(input())
    newnode = ListNode(elem,next=None)
    temp.next = newnode
    temp = temp.next

print("elements in List1: ")
temp = list1
for i in range(in_a):
    print(temp.val)
    temp = temp.next

print("elements in List2: ")
temp = list2
for i in range(in_b):
    print(temp.val)
    temp = temp.next

#coding Merging 2 sorted list
dummy = ListNode()
tail = dummy

while list1!=None and list2!=None:
    if list1.val < list2.val:
        tail.next = list1
        list1 = list1.next
    else:
        tail.next = list2
        list2 = list2.next
    tail = tail.next
if list1 != None:
    tail.next = list1
elif list2!= None:
    tail.next = list2

print("elements in merged: ")
temp = dummy.next
while temp!=None:
    print(temp.val)
    temp = temp.next