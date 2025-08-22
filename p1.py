#defining the consonants
consonants=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
#defining the vowels
vowels=['a','e','i','o','u']

word=input("Enter the word:")
def word_count(word):
    total=0
    for l in list(word):
        if(l in vowels):
          total+=3
        elif(l =="x"):
            total+=15
        else :
            total+=1
            return total
    if(len(list(word))>6 and len(list(word))<15):
        total+=10
    return total

print(word_count(word))