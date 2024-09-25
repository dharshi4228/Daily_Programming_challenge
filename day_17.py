import math
def prime(n):
    result=[]
    while n % 2==0:
        result.append(2)
        n//=2
    
    for i in range(3,int(math.sqrt(n))+1,2):
        while n% i==0:
            result.append(i)
            n=n/i
  
    if n>2:
        result.append(n)
        
    return result
def main():
    n=int(input())
    output=prime(n)
    print (output)
if __name__=="__main__":
    main()