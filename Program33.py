#enumerate function
marks=[34,56,77,54,67,8]
'''index=0
for i in marks:
    print(i)
    if(index ==3):
        print("y awesome")
    index+=1'''

# same above program with enumerate function
for index, i in enumerate(marks,start=1):
    print(i)
    if(index==3):
        print("y,awesome")