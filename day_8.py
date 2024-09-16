def reverse(s:str) -> str:
    words=s.strip().split()
    r_words=words[::-1]
    return ' '.join(r_words)
    
def main():
    s=input("Enter the sentence")
    output=reverse(s)
    print(output)

if __name__=="__main__":
    main()