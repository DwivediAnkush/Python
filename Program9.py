#strings are immutable/not chnageable
a="Ankush !" 
print(len(a))
print(a.upper()) #all letters are in capital letters
print(a.lower()) #all letters are in small letters
print(a.rstrip("!")) # remove factorial
print(a.replace("Ankush", "krishn")) # replace ankush with krishn
print(a.split(" ")) #split into parts
BlogHeading= "you are an IAS officer"
print(BlogHeading.capitalize()) # capital first letter of the string and convertes all letters into smaller ones
str="welcome to the console"
print(len(str))
print(str.center(50)) # lies the program in the center
print(len(str.center(50)))
print(a.count("Ankush")) #count how many time this term occurs
print(str.endswith("e")) # returns a boolean value i.e. TRUE or FALSE
print(str.find("to")) # gives index if term exists
print(str.isalnum()) #True only if the entire string consists of A-Z, a-z, 0-9 are present , then it returns False
print(str.isalpha()) #True only if the entire string consists of A-Z, a-z are present
print(str.islower()) #returns True if all the characters in the string are lower case, else returns False
print(str.swapcase()) # converts upper case into lower case and vice versa 