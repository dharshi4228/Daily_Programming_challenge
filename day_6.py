def find_zerosum(arr):
    index={}
    current =0
    result=[]
    
    for i in range(len(arr)):
        current +=arr[i]
        
        if current == 0:
            result.append((0,i))
        
        if current in index:
            for start in index[current]:
                result.append((start+1, i))
                
        if current not in index:
            index[current]=[]
        index[current].append(i)
    return result

def main():
    arr_input=input("Enter the array")
    arr=list(map(int,arr_input.split(',')))
    output = find_zerosum(arr)
    print(output)
if __name__=="__main__":
    main()
    