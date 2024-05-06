#tuple methods
countries= ("spain","India","Italy","england")
temp=list(countries) # change tuple into list
temp.append("Russia") #add an element
temp.pop(3) #remove element of index 3
temp[2]="finland" # change element
countries= tuple(temp) # change list into temp
print(countries)

country=("malaysia","Uganda")
Asia=countries + country #adding two tuples
print(Asia)

print(countries.count("India"))
