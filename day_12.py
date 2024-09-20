def balanced(s):
    brackets={
        '(':')',
        '[':']',
        '{':'}'
    }
    stack=[]
    for char in s:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack :
                return Flase
            top = stack.pop()
            if brackets[top] != char:
                return False 
    return len(stack)==0

def main():
    s=input("Enter the input:")
    if balanced(s):
        print("True")
    else:
        print("False")

if __name__=="__main__":
    main()
