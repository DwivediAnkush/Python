#finally code
try:
    result=10/0
except ZeroDivisionError:
    print("error: divison by zero")
finally :
    print("Finally block executed")