#file handling 2
f= open('1.txt','r')
while True:
    line=f.readline()
    if not line:
        break
    print(line)
# Note :- The readlines method reads a single line from the file. If we want to read multiple lines we can use loop.
    
f= open('1.txt','w')
lines=['line1\n','line2\n','line3\n']
f.writelines(lines)
f.close()