def dist(s,k):
    n=len(s)
    res =0
    for start in range(n):
        dist_count=0
        char_count =[0]*26
        for end in range(start,n):
            current=ord(s[end])-ord('a')
            if char_count[current]==0:
                dist_count+=1
            char_count[current] +=1
            if dist_count ==k:
                res +=1
            if dist_count >k:
                break
    return res

def main():
    s= input("Enter the string: ")
    k=int(input("distinct characters="))
    output=dist(s,k)
    print("Output",output)
  
if __name__=="__main__":
    main()