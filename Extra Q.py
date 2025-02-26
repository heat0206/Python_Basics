def words(str):
    words = str.split()
    return words
def two_words(str):
    for n in range(len(str)-1):
        {
            print(str[n],str[n+1])
        }

str1=input("Enter the string: ")
separate_words=words(str1)
two_words(separate_words)
