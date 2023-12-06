print("Count the number of characters(character frequncy) in a string using directory..\n")

def countChar(inputString):
    Count={}
    for char in inputString:
        if char in Count:
            Count[char]+=1
        else:
            Count[char]=1


    return Count
str2= input("Enter a string:")
result=countChar(str2)
print(result)
