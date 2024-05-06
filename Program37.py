# File handling in python
f=open('1.txt', 'r')  #to read a file
text=f.read()
print(text)
f.close()

f=open('1.txt', 'w')  #to write a file
text=f.write('hello world')
print(text)
f.close()

f=open('1.txt', 'a')  #to write a file
text=f.write('hello world')
print(text)
f.close()

with open('1.txt','a') as f:
    f.write("hey I am inside with") # no need to use close the file