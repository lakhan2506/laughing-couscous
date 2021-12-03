def fun1(a,b):
    return a+b
def fun2(a,b):
    return a-b
def fun3(a,b):
    return a*b
def fun4(a,b):
    return a/b
def fun5(a,b):
    return a%b

print("Operations : ");
print("\t1. sum \n\t2. subtraction \n\t3.multiply \n\t4.divide \n\t5.remnder")
choice = 0
while choice <= 6:
    choice = int(input("Enter choice(1/2/3/4): "))
    a=int(input("Enter first number : "))
    b=int(input("Enter sencond number : "))


    if choice == 1:
        print(fun1(a,b))
    elif choice == 2:
        print(fun2(a,b))
    elif choice == 3:
        print(fun3(a,b))
    elif choice == 4:
        print(fun4(a,b))
    elif choice == 5 :
        print(fun5(a,b))
    else:
        break

