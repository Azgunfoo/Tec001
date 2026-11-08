number = []
print ("Enter your numbers, press enter to quit")
while True:
    user_input = input("Enter numbers:")
    if user_input == "":
        break
    try:
        num = float(user_input)
        number.append(num)
    except ValueError:
        print("Wrong number! please try again")
if len(number) >= 5:
    number.sort(reverse=True)
    print("5 biggest numbers,(from biggest to lowest):")
    for num in number[:5]:
        print(num)
else:
    print("Not enough numbers.", len(number),"numbers")
