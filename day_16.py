def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def lcm(a,b):
    return (a*b) // gcd(a,b)
if __name__=="__main__":
    a = int(input("Enter the value"))
    b=int(input("Enter the value"))
    print("Output:",lcm(a,b))