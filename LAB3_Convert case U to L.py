#Convert case
def convert_U_to_L():
    a=input("Enter a string:")
    result=''
    for ch in a:
        ch=chr(ord(ch)+32)
        result=result+ch
    print(result)

convert_U_to_L()   
