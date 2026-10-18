print("==================================")
print(" Holiday  plan for any spare time")
print("==================================")
print()

print("Choose your holiday")
print("1- mountain")
print("2- European country")
print()

choice = int(input("choose 1 or 2"))
print()

if choice ==1:
    print("you chose 1 mountain")
    print("what to do at mountain?")
    print("1 - camping")
    print("2 - big hike")

    mountain_choice = int(input("choose 1 or 2 " ))

    print()
    if mountain_choice == 1:
        print("you chose camping")
        print("remember to ge a tent and light")
    else:
        print(" wear comfortable clothes")
        print("go and explore nature")
elif choice == 2:
    print(" you choose  your European country")
    print("1 - Italy")
    print("2 - France")
    print()

    European_choice = int(input("choose 1 or 2 : "))

if European_choice == 1:
    print("Good city to visit = Rome")
    print("fact = Italy has the smallest country")
else:
        print(" Good city to visit = paris ")
        print("fact = France is the home to disneyland")
print("===========================")
print(" Hope we found your holiday")
print("===========================")