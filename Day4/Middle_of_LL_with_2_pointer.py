class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

print("Please enter the number of elements in List: ")
in_a = int(input())


print("Please enter the elements in List: ")
elem = int(input())
list1 = ListNode(elem, next=None)
temp = list1
for i in range(in_a-1):
    elem = int(input())
    newnode = ListNode(elem,next=None)
    temp.next = newnode
    temp = temp.next

print("elements in List: ")
temp = list1
for i in range(in_a):
    print(temp.val)
    temp = temp.next

first = list1
second = list1

while(first!=None):
    first = first.next
    if first != None:
        first = first.next
    else:
        break
    second = second.next


            
print(second.val)