print("--------------------")
print(" your bike chooser  ")
print("--------------------")
print()

print("choose your vehicle!")
print("1 = bike")
print("2 = car")
print()

choose= int(input("enter 1 or 2"))
print()

if choose==1:
    print("choose your bike")
    print("1 = moutain bike")
    print("2 = stunt bike")

    bike=int(input("enter 1 or 2"))
    if bike==1:
        print("you have chosen: moutain bike")
        print("top speed:20KM per hour")
        print("fact:montain bike is best used off road")
    else:
        print("you have choosen: stunt bike")
        print("top speed: 15KM per hour")

elif choose == 2:
    print("choose your car!")
    print("1 = BMW")
    print("2 = land rover")

    car=int(input("enter 1 or 2"))
    if car==1:
        print("your car is : BMW")
        print("top speed is : 70KM per hour")
        print("use on road")
    else:
        print("your car is:land rover")
        print("top speed:90KM per hour")
        print("best used of road") 

else:
    print("invalid choice")

print(" hope we found your vehicle!")