#remove a string from an already existing one
st=input("Enter a string:")
r=input("Enter string to be removed:")
if r in st:
    print(st[:st.find(r)]+st[st.find(r)+len(r):])
else:
    print("string not present in given string")
    
