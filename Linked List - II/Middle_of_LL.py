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

count = 0
mid = 0
temp = list1
while(temp!=None):
    count = count + 1 
    temp = temp.next
    if count%2==0:
        mid = int((count/2)) + 1
    else:
        mid = int((count+1)/2)
for i in range(mid-1):
    list1 = list1.next
            
print(list1.val)