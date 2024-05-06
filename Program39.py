#seek and tell functions
with open('1.txt','r') as f:
    print(type(f))
    f.seek(10) # The seek function allows us to move the current position within a file to a specific point. The position is specified in bytes.
    data=f.read(5)
    print(data)

with open('1.txt','w') as f:
    f.write('Hello world')
with open('1.txt','r') as f: #The tell function returns position within the file.
    print(f.read())
    