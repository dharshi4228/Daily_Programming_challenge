from collections import defaultdict
def print_anagrams(wordlist):
    anagrams=defaultdict(list)
    
    for word in wordlist:
        sortword=''.join(sorted(word))
        anagrams[sortword].append(word)
    
    for i in anagrams.values():
        print(' '.join(i))
        
def main():
    listinput=input("Enter the words separated by commas:")
    wordki=listinput.strip('[]')
    wordlist=wordki.split(',')
    
    print_anagrams(wordlist)
    
if __name__=="__main__":
    main()