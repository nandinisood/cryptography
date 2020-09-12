#Program to implement ceaser cipher using additive substitution
def encrypt_add(text,s)
    translated = 
    for i in range(len(text))
        char = text[i]
        # Encrypt uppercase
        if (char.isupper())
         translated += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase
        else
            translated += chr((ord(char) + s - 97) % 26 + 97)
    return translated

ch='y'
while(ch=='y')
    text = input(Enter Text )
    s = int(input(Enter the shift pattern ))
    print()
    print(Cipher Text  + encrypt_add(text, s))
    print(Do you want to enter more (yn) )
    ch=input()