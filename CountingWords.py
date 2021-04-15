s = input("enter your introduction")
characterCount = 0
wordCount = 1
for j in s: 
    characterCount=characterCount+1
    if(j == ' '):
        wordCount = wordCount+1
print("number of words=>", wordCount)
print("number of characters",characterCount)