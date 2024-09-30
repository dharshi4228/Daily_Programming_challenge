from collections import Counter
def first_elemt(arr,k):
    count_map=Counter(arr)
    
    for i in arr:
        if count_map[i]==k:
            return i
    return -1
if __name__=='__main__':
    ar_inp=input("Enter the elements:")
    arr=list(map(int, ar_inp.split(',')))
    k= int(input("Enter the number of times the element occurs k times:"))
    print(first_elemt(arr,k))