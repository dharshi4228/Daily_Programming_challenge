def leader(arr,n):
    l=[]
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            l.append(arr[i])
    l.append(arr[n - 1])
            
    print(l)   

def main():
    arr_input=input("Enter arr=")
    arr=list(map(int,arr_input.split(",")))
    n=len(arr)
    leader(arr,n)
if __name__== "__main__":
    main()
