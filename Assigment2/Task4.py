def task4():
    a= int(input("Year: "))
    if a % 4 == 0:
        print("This is a leap year")
    elif a % 100 and a % 400 == 0:
        print("This is a leap year")
    else:
        print("This is a normal year")
task4()
