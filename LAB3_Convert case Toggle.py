#Convert case
def convert_U_to_L():
    a=input("Enter a string:")
    result=''
    for ch in a:
        if 'a'<=ch<='z':
            ch=chr(ord(ch)-32)
            result=result+ch

        elif 'A'<=ch<='Z':
            ch=chr(ord(ch)+32)
            result=result+ch
    print(result)

convert_U_to_L()
