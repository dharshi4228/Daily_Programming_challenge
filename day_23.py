from collections import deque
def printMax(arr,N,K):
    dq=deque()
    for i in range(K):
        while dq and arr[dq[-1]]<=arr[i]:
            dq.pop()
        dq.append(i)
    print(arr[dq[0]],end= " ")

    for i in range(K,N):
        while dq and dq[0]<= i-K:
            dq.popleft()
            
        while dq and arr[dq[-1]]<=arr[i]:
            dq.pop()
            
        dq.append(i)
        
        print(arr[dq[0]],end=" ")
if __name__=="__main__":
    ar_inp=input("Enter the elements:")
    arr=list(map(int, ar_inp.split(',')))
    N=len(arr)
    K=int(input("Enter k:"))
    printMax(arr,N,K)