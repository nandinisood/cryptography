#Program to implement ceaser cipher using multiplicative substitution
def encrypt_mul(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
         result += chr((ord(char) * s-65) % 26 + 65)
        else:
            result += chr((ord(char) * s - 97) % 26 + 97)
    return result

ch='y'
while(ch=='y'):
    text = input("Enter Text: ")
    s = int(input("Enter the shift pattern: "))
    print("Cipher Text: " + encrypt_mul(text, s))
    print()
    print("Do you want to enter more? (y/n): ")
    ch=input()