def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    fib=[0]*(n+1)
    fib[0]=0
    fib[1]=1
    for i in range(2,n+1):
        fib[i]=fib[i-1]+fib[i-2]
    return fib[n]
def main():
    try:
        n=int(input("Enter an integer n"))
        if 0<=n<=1000:
            result=fibonacci(n)
            print(f"The {n}-th Fibonacci number is: {result}")
        else:
            print("Pleaseenter a number number between 0 and 1000.")
    except ValueError:
        print("Invalid input")
if __name__=="__main__":
    main()