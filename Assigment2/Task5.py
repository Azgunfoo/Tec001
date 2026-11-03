import math
def task5(d,USD):
    a_pizza =float (d) * math.pi
    unit_per_m2 = a_pizza / float(USD)
    return unit_per_m2
pizza1 = task5(input("Enter your pizza 1:"),input("Enter your pizza 1 price:"))
pizza2 = task5(input("Enter your pizza 2:"),input("Enter your pizza 2 price:"))
if pizza1 > pizza2:
    print("pizza 1 have better value")
elif pizza1 == pizza2:
    print("both pizza have the same value")
else:
    print("pizza 2 have the better value")

