def add1(numbers):
    ADD=0
    for x in numbers:
        x=int(x)
        ADD=x+ADD
    return (ADD)
"""
def subtract1(numbers):
    sub=int(numbers[0])
    for y in range(1,len(numbers)):
        numbers1=numbers[y]
    #numbers.reverse()
    for x in numbers1:
        x=int(x)
        sub=sub-x
    return (sub)
"""
def multiplication1(numbers):
    mul=1
    for x in numbers:
        x=int(x)
        mul=x*mul
    return (mul)

def division1(numbers):
    div=int(numbers[0])
    ddiv=[]
    for y in range(1,len(numbers)):
        ddiv.append(numbers[y])
    for x in ddiv:
        x=int(x)
        div=div/x
    return (div)


print("Choose one of the options:")
print("0. Exit")
print("1. Add")
print("2. Subtract")
print("3. Multiplication")
print("4. Division")
print()

while (1):
    choice=input("Enter choice:")
    if choice=="0":
        quit()
    if choice in ("1" , "2" , "3" , "4"):
        print("Enter your numbers:")
        numbers=input().split()
        if choice=="1":
            print("The sum of the numbers is equal to {}".format(add1(numbers)))
        #elif choice=="2":
         #   print("The subtract of the numbers is equal to {}".format(subtract1(numbers)))
        elif choice == "3":
            print("The multiply of the numbers is equal to {}".format(multiplication1(numbers)))
        elif choice=="4":
            print("The division of the numbers is equal to {}".format(division1(numbers)))

    else:
        print("This option is invalid")

