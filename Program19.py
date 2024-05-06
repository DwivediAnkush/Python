#List methods
L=[11,34,56,78,1,1,1]
print(L)
L.append(4)# add on last
L.sort(reverse=True) #gives true if reverse of the list is sorted
L.reverse() #reverse the List
print(L.count(1))
m=L.copy() #copy a list
print(m)
L.insert(2,999) #(index,value)
L.extend(m) #L ke piiche m jud jayega
k=L+m # add two lists
print(L)