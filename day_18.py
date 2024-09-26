def divisor (n):
    divisors=[]
    for i in range(1,n+1):
        if n% i==0:
            divisors.append(i)
            
    
    return divisors
    
def main():
    n=int(input("Enter a number: "))
    s=len(divisor(n))
    print("Output: "s)
if __name__=="__main__":
    main()
    