#if- else statement
a=int(input("Enter your age"))
print("your age is ", a)
if(a>18):
    print("you can drive")
else:
    print("you are not eligible to drive")

appleprice=10
budget=200
if(budget-appleprice> 50):
    print("Add 1 kg apples to the cart")
elif(budget-appleprice>70):
    print("its okay you can buy")
else:
    print("do not add apples to the cart")
