#Convert case
def convert_L_to_U():
    a=input("Enter a string:")
    result=''
    for ch in a:
        ch=chr(ord(ch)-32)
        result=result+ch
    print(result)

convert_L_to_U()
