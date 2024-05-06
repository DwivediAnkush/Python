#for loops
name= " ankush"
for i in name:
    print(i)
    if(i=="b"):
        print("this is something special! ")

colors= ["red", "green", "blue","yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

for k in range(5):
    print(k) # always one less than actual

for k in range(1,30,3): # (starting , ending , between)
    print(k)