#global and local variables
x=4
print(x)
def hello():
    x=5
    print(x)
    print(f"The local x is {x}")
    print("hello Dwivedi")

print(f"The global x is {x}") #outside the function
hello()
print(f"The global x is {x}")

y=2 #global variable
def f():
    x=4
    global y
    y=8
    print(x)
f()
print(y)

