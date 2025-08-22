palin=input("Enter palindrome:")
if(palin is int):
    print("Is integer")
else:
    print("Is string")

def is_palindrome(palin):
    for l in list(palin):
        if(l==r in reversed(list(palin))):
            print("Is palindrome")
        else:
            print("Is not palindrome")

#is_palindrome(str(palin))
def palinverif(palin):
    if palin == palin[::-1]:
        print("Yes")
    else:
        print("No")

palinverif(palin)
