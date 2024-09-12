def connect(arr1,arr2,n1,n2):
    for i in range(n1):
        if arr1[i]>arr2[0]:
            arr1[i],arr2[0] =arr2[0],arr1[i]
            
            f_element=arr2[0]
            k=1
            while k<n2 and arr2[k] <f_element:
                arr2[k-1]=arr2[k]
                k+=1
            arr2[k-1]=f_element


def main():
    arr1_input=input("Enter arr1=")
    arr2_input=input("enter arr2=")
    arr1=list(map(int,arr1_input.split(",")))
    arr2=list(map(int,arr2_input.split(",")))
    n1=len(arr1)
    n2=len(arr2)
    connect(arr1,arr2,n1,n2)
    print("arr1=",arr1)
    print("arr2=",arr2)
    
if __name__=="__main__":
    main()


