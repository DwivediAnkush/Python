#Lists
L=[3,5,7, "Ankush", True]
print(L)
print(type(L))
print(L[0])
print(L[1])
print(L[2])
print(L[-1])
# they are mutable/changeable
if "Ankush" in L:
    print("yes")
else:
    print("no")
print(L[:])
print(L[1:-1])