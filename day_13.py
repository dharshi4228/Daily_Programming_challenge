def check_palindrome (s, low, high):
    while low<high:
        if s[low] != s[high]:
            return False
        low +=1
        high -=1
    return True
def longest_palindrome(s):
    n=len(s)
    max_length=1
    start_index=0
    
    for i in range(n):
        for j in range(i,n):
            if check_palindrome(s,i ,j)and(j-i+1)>max_length:
                
                start_index=i
                max_length=j-i+1
    return s[start_index:start_index+max_length]

def main():
    s=input("Enter the string:")
    output=longest_palindrome(s)
    print(output)
if __name__=="__main__":
    main()