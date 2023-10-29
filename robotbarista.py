#remembering my talking barista program

print("hello, I am Sally, Welcome to coffee dumpster Please choose from the menu ")
menu = "latte, expresso, black coffee, cappucino "
print(menu)
drink = input("what would you like? ")
print(drink)
drink2 = input("anything else you would like? Yes or No? ")
if drink2 == "yes":
    print("what would you like? ")
    anotherdrink = input("ok, your drink is ")
else:
    print("ok, its no lets get your first drink going ")
name = input("what is your name? ")
print("welcome to coffee dumpster "+ name +"")
if drink2 == "yes":
    print("I will have your "+ drink +" and your "+ anotherdrink +" in a moment")
else:
    print("I will have your "+ drink +" ready in a moment")

pay1 = "cash"
pay2 = "card"
pay = (input("will you be paying by cash or card? "))

if pay == "cash":
    print("please pay now, thanks "+ name +"")
    print("heres your drink "+ name +" enjoy your "+ drink +"")
    print("Thanks for coming today "+ name +", please come back")
elif pay == "card":
    print("please swipe your card "+ name +", thanks")
    print("heres your drink "+ name +", enjoy your "+ drink +"")
    print("Thanks for coming today "+ name +", please come back")
    
else:
    print("sorry we cannot serve you ")




