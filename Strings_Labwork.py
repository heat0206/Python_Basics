#Count the number of Vowels
s=input("Enter string :")
vowels=0
for ch in s:
    if ch in 'aeiouAEIOU':
        vowels=vowels+1
       

print(vowels)
