temp=int(input("enter the temperature:"))

if temp < 20:
    outfit="sweater"
    print("It is cold.")
    print("Wear a",outfit)
else:
    outfit="t-shirt"
    print("It is hot")
    print("wear a ",outfit)

is_raining=input("Is it raining? yes/no")
if is_raining=="yes":
    print("Bring an umbrela!")

if is_raining=="no":
    print("Put a hat on and put sun cream on!")
