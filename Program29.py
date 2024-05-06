# exceptional handling
a=input("enter the number ")
print("multiplication table of " ,a)
try:
  for i in range (1,11):
    print(a*i)
except:
  print("invalid input")

print("some code ")

#Note :- Exceptionb handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without the process, exception would disrupt the normal operation of a program.