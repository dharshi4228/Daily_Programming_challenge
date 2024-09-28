def re_sort(s,element):
    if len(s)==0 or element >s[-1]:
        s.append(element)
        return
    temp=s.pop()
    re_sort(s,element)
    s.append(temp)
def stack(s):
    if len(s)!=0:
        temp=s.pop()
        stack(s)
        re_sort(s,temp)
        
def printstack(s):
    for i in s[::-1]:
        print(i,end=" ")
    print()
    
if __name__=='__main__':
    inp =input("Enter the elements")
    s= list(map(int, inp.split(',')))
    stack(s)
    printstack(s)
    
