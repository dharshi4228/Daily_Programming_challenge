from collections import defaultdict
def swap (s,i,j):
    charmap=defaultdict(str)
    for idx, char in enumerate(s):
        charmap[idx] = char
    
    charmap[i], charmap[j] = charmap[j],charmap[i]
    return ''.join([charmap[k] for k in range(len(s))])
    
def permutation(s, start):
    if start == len(s) - 1:
        print(s)
        return
    
    for i in range(start, len(s)):
        
        s = swap (s, start ,i)
        permutation (s, start+1)
        s = swap (s, start, i)
        
def string(s):
    permutation(s,0)

def main():
    s=input("Enter the string")
    string(s)
    
if __name__=="__main__":
    main()