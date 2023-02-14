class Stack:
    def __init__(self):
        self.elements = []
    def push(self,data):
        self.elements.append(data)
    def pop(self):
        return self.elements.pop()
    def size(self):
        return len(self.elements)
    def empty(self):
        return True if self.size() == 0 else False

Forward_Stack = Stack()
Backward_Stack = Stack()

tc = int(input())

current = "c:"

a=input()
for i in range(tc):
    print("Case " + str(i+1) + ":")
    while(a!="QUIT"):
        length = len(a);
        if a[0:4] == "OPEN":
            #print("YES")
            dir = a[5:length]
            Backward_Stack.push(current)
            Forward_Stack = Stack()
            current = dir
            print(current)
        elif a == "BACK":
            if Backward_Stack.empty()==True:
                print("Ignored")
            else:
                Forward_Stack.push(current)
                current = Backward_Stack.pop()
                print(current)
        elif a == "FORWARD":
            if Forward_Stack.empty()==True:
                print("Ignored")
            else:
                Backward_Stack.push(current)
                current = Forward_Stack.pop()
                print(current)
        a=input()
    

