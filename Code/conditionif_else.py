age = int(input("Enter your age:\t"))

if age <= 18:
    print("Age is minor\t", age)
elif age > 18 and age <= 50:
    print("Age is Mid:\t", age)
elif age > 50 and age <=75:
    print("Age is veteran\t", age)
else:
    print("Age is super veteran\t", age)