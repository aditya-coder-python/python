total = 3
count = total
print ("you have ",count,"chores to complete")
completed = 0
chore_num = 1

while chore_num <= total:
    if chore_num == 1:
        next = "unloading the dishwasher"
    elif chore_num == 2:
        next = "cleaning your bed "
    else :
        next = "cleaning your desk"

    answer = input(f"have you finished?{next} yes or no ?")
    if answer =="yes":
        completed += 1
        chore_num += 1
        print("good job !")
    else:
        print (" keep on going you can do this!")
    print (" you have", total - completed)
    print()
print("all chores complete well done")