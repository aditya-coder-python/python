print("===smart school planner===")

print("I will ask you 3  questions.")
day=input("what is the day today ?").strip().capitalize()
weather=input("what is the weather ?").strip().lower()
homework=input("have you done your homework?").strip().lower()

print()
print("===plan for ",day,"====")
print("-"*35)

if day in ("Saturday", "Sunday"):
    print("day type: weekend,have a nice time!")
elif day == "Monday":
    print("day type :  school first day get ready for the week ahead! It is p.e day! hooray!")
elif day == "Friday":
    print("day type = award ceremony today!")
elif day in ("Tuesday","Wednesday" ,"Thursday"):
    print("a normal school day,keep going")
else:
    print("day not recognise pleas try again ")

if weather == "cloudy" or weather =="rainy":
    print("tip: bring an umbrella ")

if not (homework == "yes"):
    print(" stay in the house")

if weather =="sunny" and homework =="yes":
    print("go to your local park!")