class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    def size(self):
        return len(self.items)
def reverse_stack(stack):
    if stack.is_empty():
            
        return 
    top=stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top)
def insert_at_bottom(stack,item):
    if stack.is_empty():
        stack.push(item)
    else:
        top=stack.pop()
        insert_at_bottom(stack,item)
        stack.push(top)
def main():
    s=Stack()
    inp =input("Enter the elements")
    sn= list(map(int, inp.split(',')))
    for i in sn:
        s.push(i)
    reverse_stack(s)
    print("Reversed Stack:",s.items)
if __name__=="__main__":
    main()
    
