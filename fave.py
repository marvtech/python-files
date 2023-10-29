#while programming in python3
num = int(input("what is your first number? "))
num2 = int(input("what is your second number? "))
favorite = num or num2
choice = int(input("which of the two is your best number? " ))
if choice == num:
    print("your fave is", +num)
elif choice == num2:
    print("your fave is", +num2)
else:
    print("you didnt tell us your fave")
name = input("what is your name? ")
if choice == num:
    print ("your name is " + name + " and your favorite number is ", +num)
elif choice == num2:
    print(" your name is " + name + " and your favorite number is ", +num2)
else:
    print(name+ " didnt tell us a favorite number")